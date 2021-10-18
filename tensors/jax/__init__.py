import jaxlib

from jax.numpy import (
    array as tensor
)
from jax import (
    dlpack
)

TENSOR_CLASSES = [jaxlib.xla_extension.DeviceArray]


from .. import _backend
_backend.add_common_members(locals())
