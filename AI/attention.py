import torch
from typing import List
from torch import nn
import math
import torch.functional as F

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
attention = multi_head_attention(64, 8)

print("Input shape:", X.shape)
X_out = attention(X, X, X)
print("Output shape:", X_out.shape)
