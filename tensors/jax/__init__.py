import jax as framework
import jaxlib

from jax.numpy import (
    array as tensor,

    argmax,
    einsum,
)
from jax import (
    dlpack
)

Tensor = jaxlib.xla_extension.DeviceArray

from .. import _backend
_backend.add_common_members(locals())
