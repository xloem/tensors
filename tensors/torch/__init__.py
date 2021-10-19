import torch as framework

from torch import (
    tensor,
    Tensor,

    arange,

    cat as concat,
    stack,

    argmax,
    einsum,
)
from torch.nn.functional import (
    softmax,
)
from torch.utils import (
    dlpack
)


from .. import _backend

_backend.rename_kws(locals(), 'argmax concat stack softmax', axis='dim', dim=0)

_backend.add_common_members(locals())
