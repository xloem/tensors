import tensors.jax, tensors.torch

TENSOR_CLASS_BACKENDS = {}

def get_backend(tensor):
    return TENSOR_CLASS_BACKENDS[type(tensor)]

#def backend_common(backend):
#    TENSOR_CLASSES = []
#
#    def is_backend(tensor):
#        '''
#        Identify whether a tensor belongs to this backend.
#
#        :param tensor: tensor to check
#        :returns: True if the tensor belongs to this backend
#        '''
#        for cls in backend.TENSOR_CLASSES:
#            if isinstance(tensor, cls):
#                return True
#        return False
#
#    def to_backend(tensor):
#        '''
#        Convert a tensor to this backend
#
#        :param tensor: tensor to convert
#        :returns: tensor in backend-specific format
#        '''
#        # dlpack is a universal tensor interchangen standard
#        dlpack = get_backend(tensor).dlpack.to_dlpack(tensor)
#        return backend.dlpack.from_dlpack(dlpack)
#
#    return locals()

for backend in tensors.jax, tensors.torch:
    TENSOR_CLASS_BACKENDS.update({cls : backend for cls in backend.TENSOR_CLASSES})

#    for name, common in backend_common(backend).items():
#        if not hasattr(backend, name):
#            # provide common item if it is not implemented
#            setattr(backend, name, common)
#        else:
#            impl = getattr(backend, name)
#            if hasattr(common, '__doc__'):
#                # provide documentation if it is implemented without docs
#                if not hasattr(impl, '__doc__'):
#                    impl.__doc__ = common.__doc__
