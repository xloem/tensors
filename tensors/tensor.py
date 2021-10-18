from . import backends

__all__ = []
for backend in backends:
    locals()[backend.name] = backend.tensor
    __all__.append(backend.name)
