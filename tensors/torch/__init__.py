import torch as framework

from torch import (
    tensor,
    Tensor,

    argmax,
    stack,
    einsum,
)
from torch.nn.functional import (
    softmax,
)
from torch.utils import (
    dlpack
)


from .. import _backend

_backend.rename_kws(locals(), 'argmax stack softmax', axis='dim', dim=0)

_backend.add_common_members(locals())
