import numpy as np
import torch
from typing import List

def softmax(x: List):
    '''
    Math function: softmax
    Softmax(x) = exp(x) / sum(exp(x))

    在pytorch库的实现中, 为了数值稳定性, 会对x减去最大值, 使得exp(x)不会溢出
    '''
    list_max = max(x)

    exp_list = [np.exp(ele-list_max) for ele in x]
    
    sum_list = sum(exp_list)

    return_list = [ele/sum_list for ele in exp_list]

    return return_list

# Test
x = [1,2,3,4,5]

my_softmax = softmax(x)

x_tensor = torch.tensor(x, dtype=torch.float32)
torch_softmax = torch.softmax(x_tensor, dim=0).numpy()

print("My softmax:", my_softmax)
print("Torch softmax:", torch_softmax)