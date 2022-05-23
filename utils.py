import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parameter import Parameter

class SparseGraphConvolution(nn.Module):
    def __init__(self, in_features: int, out_features: int, bias: bool = False):
        super(SparseGraphConvolution, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = Parameter(torch.FloatTensor(in_features, out_features))
        if bias:
            self.bias = Parameter(torch.FloatTensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.weight.data)
        if self.bias is not None:
            nn.init.constant_(self.bias.data, 0)

    def forward(self, input: torch.sparse.FloatTensor, adj: torch.sparse.FloatTensor) -> torch.Tensor:
        support = torch.spmm(input, self.weight)
        output = torch.spmm(adj, support)
        if self.bias is not None:
            return output + self.bias
        else:
            return output

    def __repr__(self):
        return self.__class__.__name__ + ' (' \
               + str(self.in_features) + ' -> ' \
               + str(self.out_features) + ')'