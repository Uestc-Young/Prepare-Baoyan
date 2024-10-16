import torch
from typing import List
from torch import nn
import math
import torch.functional as F

class Scale_Dot_Attention(nn.Module):
    def __init__(self, d_model: int):
        super().__init__()
        self.d_model = d_model

        self.W_Q = nn.Linear(self.d_model, self.d_model)
        self.W_K = nn.Linear(self.d_model, self.d_model)
        self.W_V = nn.Linear(self.d_model, self.d_model)
    
    def forward(self, x):

        B, seq_len, dim = x.shape

        q = self.W_Q(x) # (B, L, D)
        k = self.W_K(x) # (B, L, D)
        v = self.W_V(x) # (B, L, D)

        attention_score = torch.matmul(q, k.permute(0, 2, 1)) / math.sqrt(dim)
        attention_score = torch.softmax(attention_score, dim = -1)

        return torch.matmul(attention_score, v)


class multi_head_attention(nn.Module):
    '''
    Re-Implementation of Multi-Head Attention

    Math Formulation:
    Attention(Q, K, V) = softmax(Q*K^T / sqrt(d_k))*V 

    Args:
        d_model: int - The size of the input dimension
        n_heads: int - The number of heads to split the input 
    '''
    def __init__(self, d_model: int, n_heads: int, type:str = "masked_attention") -> None:
        super(multi_head_attention, self).__init__()

        self.d_model = d_model
        self.n_heads = n_heads
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_out = nn.Linear(d_model, d_model)
        self.softmax = nn.Softmax(dim=-1)


    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        batchsize, seq_len, dim = q.shape
        n_d = self.d_model // self.n_heads

        query = self.w_q(q)
        key = self.w_k(k)
        value = self.w_v(v)

        query = query.view(batchsize, seq_len, self.n_heads, n_d).permute(0, 2, 1, 3) # (B, n_heads, seq_len, n_d)
        key = key.view(batchsize, seq_len, self.n_heads, n_d).permute(0, 2, 1, 3) # (B, n_heads, seq_len, n_d)
        value = value.view(batchsize, seq_len, self.n_heads, n_d).permute(0, 2, 1, 3) # (B, n_heads, seq_len, n_d)

        attention_score = query @ key.transpose(2, 3) / math.sqrt(n_d) # 除n_d是为了让方差变小

        # 构造decoder中的attention
        mask = torch.tril(torch.ones(seq_len, seq_len, dtype=bool))
        score = attention_score.masked_fill(mask == 0, float("-inf"))
        score = self.softmax(score) @ value

        score = score.permute(0, 2, 1, 3).contiguous().view(batchsize, seq_len, dim)
        
        attention_out = self.w_out(score)
        return attention_out


# Test
X = torch.randn(256, 128, 64)
# attention = multi_head_attention(64, 8)
attention = Scale_Dot_Attention(64)

print("Input shape:", X.shape)
X_out = attention(X)
print("Output shape:", X_out.shape)
