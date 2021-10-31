import inspect

backend_names = set(('jax', 'tensorflow', 'torch'))

def load_backend_by_name(name : str):
    if name == 'jax':
        import tensors.jax as backend
    elif name == 'tensorflow':
        import tensors.tensorflow as backend
    elif name == 'torch':
        import tensors.torch as backend
    else:
        raise Exception('Unknown backend: ' + name)
    if name not in backends_by_name:
        register(backend)
    return backend

backends_by_name = {}
backends_by_tensor_class = {}
backends_by_device_class = {}

def load_all_backends():
    return [load_backend_by_name(name) for name in backend_names]

def register(backend):
    '''
    Registers a backend after it is loaded.
    '''
    backends_by_tensor_class[backend.Tensor] = backend
    backends_by_device_class[backend.Device] = backend
    backends_by_name[backend.name] = backend

    import tensors

    try:
        tensors.__all__.extend(backend.name)
    except Exception:
        # still importing
        pass

    for name in dir(backend):
        member = getattr(backend, name)
        if backend.name in name and backend.name != name:
            setattr(tensors, name, member)

def set_default(backend):
    import sys
    import tensors
    tensors.default = backend
    sys.modules['tensors.default'] = tensors.default
    #for name, member in backend.__dict__.items():
    #    if name[0] != '_' and callable(member):
    #        setattr(tensors, name, member)

def load_new_backends():
    '''
    Enumerates loaded tensor packages and imports a tensors backend for any new ones found.

    :returns: list of new tensors backend modules
    '''
    import sys

    new_backends = backend_names.difference(backends_by_name.keys())
    new_backends.intersection_update(sys.modules.keys())

    new_backends = [load_backend_by_name(name) for name in new_backends]
    return new_backends

'''
funcname(x1, x2, /, *, key1=-1, key2=None)

    Parameters

    x1 : array
        description
    x2 : array
        description
    key1 : int
        description
    key2 : Optional[str]
        description

    Returns

    out : array
        description
'''

class array_api:
    def __init__(self, impl):
        self._impl = impl
    def __getitem__(self, idx):
        return self.__class__(self._impl[idx])
    def __setitem__(self, idx, val):
        self._impl[idx] = self._to_impl(val)
    @property
    def dtype(self):
        raise NotImplemented
    #@property
    #def device(self):
    [exec(compile(inspect.cleandoc(f'''
            def {opname}(x1, x2):
                return x1.__class__(x1._impl {op} x1.to_impl(x2))
            __{opname}__ = {opname}
            '''), __file__, 'exec'),
        globals(), locals())
        for opname, op in {
            'lt':'<', 'le':'<=', 'gt':'>', 'ge':'>=',
            'eq':'==', 'ne':'!='
        }.items()
    ]
    # wrap remaining binary operators
    [exec(compile(inspect.cleandoc(f'''
            def {opname if opname not in ('and', 'or') else opname + '_'}(x1, x2):
                return x1.__class__(x1._impl {op} x1.to_impl(x2))
            __{opname}__ = {opname if opname not in ('and', 'or') else opname + '_'}
            def __r{opname}__(x2, x1):
                return x2.__class__(x1 {op} x2._impl)
            def __i{opname}__(x1, x2):
                x1._impl {op} x1.to_impl(x2)
            '''), __file__, 'exec'),
        globals(), locals())
        for opname, op in {
            'add':'+', 'sub':'-',
            'mul':'*', 'truediv':'/', 'floordiv':'//',
            'pow':'**', 'matmul':'@', 'mod':'%',
            'and':'&', 'or':'|', 'xor':'^',
            'lshift':'<<', 'rshift':'>>'
        }.items()
    ]
    # wrap unary operators
    [exec(compile(inspect.cleandoc(f'''
            def {opname}(x):
                return x.__class__({op}x._impl)
            __{opname}__ = {opname}
            '''), __file__, 'exec'),
        globals(), locals())
        for opname, op in {
            'pos':'+', 'neg':'-', 'invert':'~'
        }.items()
    ]

    @staticmethod
    def _to_impl(wrapped_val):
        if isinstance(wrapped_val, array_api):
            return wrapped_val._impl
        else:
            return wrapped_val
    def __getattr__(self, attr_name):
        cls = self.__class__
        subctx = dict(cls = cls)
        if callable(result):
            exec(compile(inspect.cleandoc(f'''
            def ${attr_name}(self, *params, **kwparams):
                return cls(self._impl.${attr_name}(*params, **kwparams))
            '''), self.__class__.__module__, 'single'), None, subctx)
            wrapper = subctx[attr_name]
        else:
            exec(compile(inspect.cleandoc(f'''
            def ${attr_name}(self):
                return cls(self._impl.${attr_name})
            '''), self.__class__.__module__, 'single'), None, subctx)
            wrapper = property(subctx[attr_name])
        setattr(cls, attr_name, wrapper)
        return getattr(self, attr_name)

def clone_basic(member, globals):
    import types
    if type(member) is types.FunctionType:
        instance = types.FunctionType(member.__code__, globals, member.__name__, member.__defaults__, member.__closure__)
        instance.__annotations__ = member.__annotations__
        instance.__dict__ = {**member.__dict__}
        instance.__doc__ = member.__doc__
        instance.__kwdefaults__ = member.__kwdefaults__
        # is something else needed if it's a class function?
    elif type(member) is type:
        instance = type(
            member.__name__,
            (*member.__bases__,member),
            { name: clone_basic(member, globals) for name, member in member.__dict__.items() }
        )
    else:
        instance = member
    return instance

def module_inherit(globals, supermodule):
    for name, member in supermodule.__dict__:
        if name == '__all__':
            __all__ = globals.get(name, globals)
            __all__ = list(set(__all__) | set(member))
            globals['__all__'] = __all__
        elif name not in globals:
            globals[name] = clone_basic(member, globals)

def common_members(
        Tensor : type,
        tensor : callable,
        Device : type,
        dlpack,
        hwaccel_present : callable,
        __name__ : str = '',
        **kw
    ) -> dict:
    '''
    Define and return common members for backend modules.

    :param kw: **locals() from the backend
    :returns: A dict of common members to add
    '''
    del kw
    name = __name__.split('.')[-1]

    @backend_doc(name)
    def is_backend(object) -> bool:
        '''
        Identify whether an object is from this backend
        '''
        return isinstance(tensor, Tensor) or isinstance(tensor, Device)

    @backend_doc(name)
    def to_backend(foreign_object) -> Tensor:
        '''
        Convert a tensor to this backend
        '''
        from . import get_backend, _dlpack
        # dlpack is a universal tensor interchangen standard
        foreign_backend = get_backend(foreign_tensor)
        dlpack_tensor = foreign_backend.dlpack.to_dlpack(foreign_tensor)

        try:
            return dlpack.from_dlpack(dlpack_tensor)
        except Exception as exception:
            if not hwaccel_present():
                # if the foreign tensor is on a gpu
                # and the destination backend doesn't have access to hardware acceleration
                # it will need to be downloaded to the cpu
                dlpack_cptr = _dlpack.ctypes.cast(_dlpack.PyCapsule_GetPointer(dlpack_tensor, b'dltensor'), _dlpack.ctypes.POINTER(_dlpack.DLManagedTensor))
                dtype = dlpack_cptr.contents.dl_tensor.ctx.device_type
                if not (dtype.value & dtype.kDLCPU):
                    import warnings
                    warnings.warn('Copy tensor from ' + foreign_backend.name + ' GPU to ' + name + ' CPU.')
                    dlpack_tensor = foreign_backend.dlpack.to_dlpack(foreign_tensor.clone().cpu())
                    return dlpack.from_dlpack(dlpack_tensor)
            raise

    backend_tensor = tensor

    return locals()

def backend_doc(name):
    def mutate_doc(func):
        if func.__doc__ is not None and 'this backend' in func.__doc__:
            func.__doc__ = func.__doc__.replace('this backend', name)
        return func
    return mutate_doc

def rename_kws(locals, func_names, **kwparams):
    import inspect
    import re

    dflts = {}
    # let src=default set manual defaults
    for src, dflt in [*kwparams.items()]:
        if src in kwparams.values():
            dflts[src] = dflt
            del kwparams[src]
    src_by_dst = kwparams
    dst_by_src = {src:dst for dst,src in src_by_dst.items()}

    # it's possible more things can be pulled out of the below loop
    for func_name in func_names.split(' '):
        func = locals[func_name]

        # update defaults to match function documentation if reasonable to do so
        func_dflts = {**dflts}
        try:
            sig = inspect.signature(func)
            for src, param in sig.parameters.items():
                func_dflts[src] = param.default
        except:
            sig = None

        # make a list of kwparam mutations with defaults
        map = [(src, dst, func_dflts[src]) for dst, src in src_by_dst.items()]

        # wrapper function
        def make_wrapper(func, map):
            def mutated(*params, **kwparams):
                for src, dst, dflt in map:
                    kwparams[src] = kwparams.pop(dst, dflt)
                return func(*params, **kwparams)
            return mutated
        mutated = make_wrapper(func, map)

        # update metadata of wrapper function for docs etc
        mutated.__name__ = func_name
        if sig is not None:
            # replace parameter names in signature
            mutated.__signature__ = sig.replace(parameters=[
                param.replace(name=dst_by_src[param.name])
                    if param.name in dst_by_src
                    else param
                for param in sig.parameters.values()
            ])
        for dst, src in kwparams.items():
            mutated.__doc__ = re.sub(src + '([^a-zA-Z_])', dst + '\\1', func.__doc__)

        # replace func with mutated
        locals[func_name] = mutated

def add_common_members(locals : dict):
    '''
    Add common members to a backend.
    
    :param locals: locals() from within the backend
    '''
    __all__ = locals.setdefault('__all__', list(locals.keys()))
    members = common_members(**locals)
    for name, member in [*members.items()]:
        if 'backend' in name:
            name2 = name.replace('backend', members['name'])
            members[name2] = member
    locals.update(members)
    __all__.extend(members.keys())

def get_global_stubs():
    '''
    Create and return wrapper functions for backend-named functions.

    Each one, when called, imports the backend and hands its parameters off.

    :returns: dict of functions
    '''
    results = {}
    def stub(backend_name, function_name):
        def wrapper(*params, **kwparams):
            '''
            Backend will be loaded when called.  No documentation yet.
            '''
            backend = load_backend_by_name(backend_name)
            func = getattr(backend, function_name)
            return func(*params, **kwparams)
        return wrapper
    for name in common_members(None, None, None, None, None):
        if 'backend' in name:
            for backend_name in backend_names:
                backend_func_name = name.replace('backend', backend_name)
                results[backend_func_name] = stub(backend_name, name)
    return results
