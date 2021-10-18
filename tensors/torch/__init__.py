import torch

from torch import (
    tensor
)
from torch.utils import (
    dlpack
)

TENSOR_CLASSES = [torch.Tensor]


from .. import _backend
_backend.add_common_members(locals())
