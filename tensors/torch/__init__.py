import torch as framework

from torch import (
    tensor,
    Tensor,

    argmax,
    einsum,
    stack,
)
from torch.utils import (
    dlpack
)


from .. import _backend
_backend.add_common_members(locals())
