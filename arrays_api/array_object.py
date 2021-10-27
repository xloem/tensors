class Array:

    def __iadd__(self, other):
        """``+=``. May be implemented via ``__iadd__``."""
        raise NotImplementedError

    def __isub__(self, other):
        """``-=``. May be implemented via ``__isub__``."""
        raise NotImplementedError

    def __imul__(self, other):
        """``*=``. May be implemented via ``__imul__``."""
        raise NotImplementedError

    def __itruediv__(self, other):
        """``/=``. May be implemented via ``__itruediv__``."""
        raise NotImplementedError

    def __ifloordiv__(self, other):
        """``//=``. May be implemented via ``__ifloordiv__``."""
        raise NotImplementedError

    def __ipow__(self, other):
        """``**=``. May be implemented via ``__ipow__``."""
        raise NotImplementedError

    def __imatmul__(self, other):
        """``@=``. May be implemented via ``__imatmul__``."""
        raise NotImplementedError

    def __imod__(self, other):
        """``%=``. May be implemented via ``__imod__``."""
        raise NotImplementedError

    def __iand__(self, other):
        """``&=``. May be implemented via ``__iand__``."""
        raise NotImplementedError

    def __ior__(self, other):
        """``|=``. May be implemented via ``__ior__``."""
        raise NotImplementedError

    def __ixor__(self, other):
        """``^=``. May be implemented via ``__ixor__``."""
        raise NotImplementedError

    def __ilshift__(self, other):
        """``<<=``. May be implemented via ``__ilshift__``."""
        raise NotImplementedError

    def __irshift__(self, other):
        """``>>=``. May be implemented via ``__irshift__``."""
        raise NotImplementedError

    def __radd__(self, other):
        """``__radd__``"""
        raise NotImplementedError

    def __rsub__(self, other):
        """``__rsub__``"""
        raise NotImplementedError

    def __rmul__(self, other):
        """``__rmul__``"""
        raise NotImplementedError

    def __rtruediv__(self, other):
        """``__rtruediv__``"""
        raise NotImplementedError

    def __rfloordiv__(self, other):
        """``__rfloordiv__``"""
        raise NotImplementedError

    def __rpow__(self, other):
        """``__rpow__``"""
        raise NotImplementedError

    def __rmatmul__(self, other):
        """``__rmatmul__``"""
        raise NotImplementedError

    def __rmod__(self, other):
        """``__rmod__``"""
        raise NotImplementedError

    def __rand__(self, other):
        """``__rand__``"""
        raise NotImplementedError

    def __ror__(self, other):
        """``__ror__``"""
        raise NotImplementedError

    def __rxor__(self, other):
        """``__rxor__``"""
        raise NotImplementedError

    def __rlshift__(self, other):
        """``__rlshift__``"""
        raise NotImplementedError

    def __rrshift__(self, other):
        """``__rrshift__``"""
        raise NotImplementedError

    @property
    def dtype(self):
        """dtype
        *****
        
        Data type of the array elements.
        
        
        Returns
        =======
        
        *   **out**: *<dtype>*
        
            *   array data type."""
        raise NotImplementedError

    @property
    def device(self):
        """device
        ******
        
        Hardware device the array data resides on.
        
        
        Returns
        =======
        
        *   **out**: *<device>*
        
            *   a ``device`` object (see device-support)."""
        raise NotImplementedError

    @property
    def mT(self):
        """mT
        **
        
        Transpose of a matrix (or a stack of matrices).
        
        If an array instance has fewer than two dimensions, an error should be
        raised.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   array whose last two dimensions (axes) are permuted in reverse
                order relative to original array (i.e., for an array instance
                having shape ``(..., M, N)``, the returned array must have
                shape ``(..., N, M)``). The returned array must have the same
                data type as the original array."""
        raise NotImplementedError

    @property
    def ndim(self):
        """ndim
        ****
        
        Number of array dimensions (axes).
        
        
        Returns
        =======
        
        *   **out**: *int*
        
            *   number of array dimensions (axes).
        
        *TODO: need to more carefully consider this in order to accommodate,
        e.g., graph tensors where the number of dimensions may be dynamic.*"""
        raise NotImplementedError

    @property
    def shape(self):
        """shape
        *****
        
        Array dimensions.
        
        
        Returns
        =======
        
        *   **out**: *Union[ Tuple[ int, …], <shape> ]*
        
            *   array dimensions as either a tuple or a custom shape object.
                If a shape object, the object must be immutable and must
                support indexing for dimension retrieval.
        
        *TODO: need to more carefully consider this in order to accommodate,
        e.g., graph tensors where a shape may be dynamic.*"""
        raise NotImplementedError

    @property
    def size(self):
        """size
        ****
        
        Number of elements in an array. This must equal the product of the
        array’s dimensions.
        
        
        Returns
        =======
        
        *   **out**: *int*
        
            *   number of elements in an array.
        
        *TODO: need to more carefully consider this in order to accommodate,
        e.g., graph tensors where the number of elements may be dynamic.*"""
        raise NotImplementedError

    @property
    def T(self):
        """T
        *
        
        Transpose of the array.
        
        The array instance must be two-dimensional. If the array instance is
        not two-dimensional, an error should be raised.
        
        Note: Limiting the transpose to two-dimensional arrays (matrices)
            deviates from the NumPy et al practice of reversing all axes for
            arrays having more than two-dimensions. This is intentional, as
            reversing all axes was found to be problematic (e.g., conflicting
            with the mathematical definition of a transpose which is limited
            to matrices; not operating on batches of matrices; et cetera). In
            order to reverse all axes, one is recommended to use the
            functional ``permute_dims`` interface found in this specification.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   two-dimensional array whose first and last dimensions (axes)
                are permuted in reverse order relative to original array. The
                returned array must have the same data type as the original
                array."""
        raise NotImplementedError

    def __abs__(self, /):
        """__abs__(self, /)
        ****************
        
        Calculates the absolute value for each element of an array instance
        (i.e., the element-wise result has the same magnitude as the
        respective element but has positive sign).
        
        Note: For signed integer data types, the absolute value of the minimum
            representable integer is implementation-dependent.
        
        
        Special Cases
        =============
        
        For floating-point operands, let ``self`` equal ``x``.
        
        *   If ``x_i`` is ``NaN``, the result is ``NaN``.
        
        *   If ``x_i`` is ``-0``, the result is ``+0``.
        
        *   If ``x_i`` is ``-infinity``, the result is ``+infinity``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise absolute value. The
                returned array must have the same data type as ``self``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `abs(x) <#abs-x>`_."""
        raise NotImplementedError

    def __add__(self, other, /):
        """__add__(self, other, /)
        ***********************
        
        Calculates the sum for each element of an array instance with the
        respective element of the array ``other``.
        
        
        Special Cases
        =============
        
        For floating-point operands, let ``self`` equal ``x1`` and ``other``
        equal ``x2``.
        
        *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the
            result is ``NaN``.
        
        *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the
            result is ``NaN``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the
            result is ``+infinity``.
        
        *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the
            result is ``-infinity``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is a finite number, the
            result is ``+infinity``.
        
        *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is a finite number, the
            result is ``-infinity``.
        
        *   If ``x1_i`` is a finite number and ``x2_i`` is ``+infinity``, the
            result is ``+infinity``.
        
        *   If ``x1_i`` is a finite number and ``x2_i`` is ``-infinity``, the
            result is ``-infinity``.
        
        *   If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is
            ``-0``.
        
        *   If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is
            ``+0``.
        
        *   If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is
            ``+0``.
        
        *   If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is
            ``+0``.
        
        *   If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is a nonzero
            finite number, the result is ``x2_i``.
        
        *   If ``x1_i`` is a nonzero finite number and ``x2_i`` is either
            ``+0`` or ``-0``, the result is ``x1_i``.
        
        *   If ``x1_i`` is a nonzero finite number and ``x2_i`` is ``-x1_i``,
            the result is ``+0``.
        
        *   In the remaining cases, when neither ``infinity``, ``+0``, ``-0``,
            nor a ``NaN`` is involved, and the operands have the same
            mathematical sign or have different magnitudes, the sum must be
            computed and rounded to the nearest representable value according
            to IEEE 754-2019 and a supported round mode. If the magnitude is
            too large to represent, the operation overflows and the result is
            an ``infinity`` of appropriate mathematical sign.
        
        Note: Floating-point addition is a commutative operation, but not always
            associative.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance (augend array). Should have a numeric data
                type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   addend array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise sums. The returned array
                must have a data type determined by `Type Promotion Rules
                <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `add(x1, x2) <#add-x1-x2>`_."""
        raise NotImplementedError

    def __and__(self, other, /):
        """__and__(self, other, /)
        ***********************
        
        Evaluates ``self_i & other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have an integer or boolean data type.
        
        *   **other**: *Union[ int, bool, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have an integer or
                boolean data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `bitwise_and(x1, x2)
            <#logical-and-x1-x2>`_."""
        raise NotImplementedError

    def __array_namespace__(self, /, *, api_version=None):
        """__array_namespace__(self, /, *, api_version=None)
        *************************************************
        
        Returns an object that has all the array API functions on it.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance.
        
        *   **api_version**: *<Optional[str]>*
        
            *   string representing the version of the array API specification
                to be returned, in ``'YYYY.MM'`` form, for example,
                ``'2020.10'``. If it is ``None``, it should return the
                namespace corresponding to latest version of the array API
                specification.  If the given version is invalid or not
                implemented for the given module, an error should be raised.
                Default: ``None``.
        
        
        Returns
        =======
        
        *   **out**: *<object>*
        
            *   an object representing the array API namespace. It should have
                every top-level function defined in the specification as an
                attribute. It may contain other public names as well, but it
                is recommended to only include those names that are part of
                the specification."""
        raise NotImplementedError

    def __bool__(self, /):
        """__bool__(self, /)
        *****************
        
        Converts a zero-dimensional boolean array to a Python ``bool`` object.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   zero-dimensional array instance. Must have a boolean data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<bool>*
        
            *   a Python ``bool`` object representing the single element of
                the array."""
        raise NotImplementedError

    def __dlpack__(self, /, *, stream=None):
        """__dlpack__(self, /, *, stream=None)
        ***********************************
        
        Exports the array for consumption by `from_dlpack(x, /)
        <#function-from-dlpack>`_ as a DLPack capsule.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance.
        
        *   **stream**: *Optional[ Union[ int, Any ]]*
        
            *   for CUDA and ROCm, a Python integer representing a pointer to
                a stream, on devices that support streams. ``stream`` is
                provided by the consumer to the producer to instruct the
                producer to ensure that operations can safely be performed on
                the array (e.g., by inserting a dependency between streams via
                “wait for event”). The pointer must be a positive integer or
                ``-1``. If ``stream`` is ``-1``, the value may be used by the
                consumer to signal “producer must not perform any
                synchronization”. The ownership of the stream stays with the
                consumer.
        
                On CPU and other device types without streams, only ``None``
                is accepted.
        
                For other device types which do have a stream, queue or
                similar synchronization mechanism, the most appropriate type
                to use for ``stream`` is not yet determined. E.g., for SYCL
                one may want to use an object containing an in-order
                ``cl::sycl::queue``. This is allowed when libraries agree on
                such a convention, and may be standardized in a future version
                of this API standard.
        
                Device-specific notes:
        
                CUDA:
        
                *   ``None``: producer must assume the legacy default stream
                    (default).
        
                *   ``1``: the legacy default stream.
        
                *   ``2``: the per-thread default stream.
        
                *   ``> 2``: stream number represented as a Python integer.
        
                ``0`` is disallowed due to its ambiguity: ``0`` could mean
                either ``None``, ``1``, or ``2``.
        
                ROCm:
        
                *   ``None``: producer must assume the legacy default stream
                    (default).
        
                *   ``0``: the default stream.
        
                *   ``> 2``: stream number represented as a Python integer.
        
                Using ``1`` and ``2`` is not supported.
        
                Tip: It is recommended that implementers explicitly handle
                    streams. If they use the legacy default stream, specifying
                    ``1`` (CUDA) or ``0`` (ROCm) is preferred. ``None`` is a
                    safe default for developers who do not want to think about
                    stream handling at all, potentially at the cost of more
                    synchronization than necessary.
        
        
        Returns
        =======
        
        *   **capsule**: *<PyCapsule>*
        
            *   a DLPack capsule for the array. See data-interchange for
                details."""
        raise NotImplementedError

    def __dlpack_device__(self, /):
        """__dlpack_device__(self, /)
        **************************
        
        Returns device type and device ID in DLPack format. Meant for use
        within `from_dlpack(x, /) <#function-from-dlpack>`_.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance.
        
        
        Returns
        =======
        
        *   **device**: *Tuple[enum.IntEnum, int]*
        
            *   a tuple ``(device_type, device_id)`` in DLPack format. Valid
                device type enum members are:
        
                ::
        
                    CPU = 1
                    CUDA = 2
                    CPU_PINNED = 3
                    OPENCL = 4
                    VULKAN = 7
                    METAL = 8
                    VPI = 9
                    ROCM = 10"""
        raise NotImplementedError

    def __eq__(self, other, /):
        """__eq__(self, other, /)
        **********************
        
        Computes the truth value of ``self_i == other_i`` for each element of
        an array instance with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. May have any data type.
        
        *   **other**: *Union[ int, float, bool, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). May have any data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type of ``bool``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `equal(x1, x2) <#equal-x1-x2>`_."""
        raise NotImplementedError

    def __float__(self, /):
        """__float__(self, /)
        ******************
        
        Converts a zero-dimensional floating-point array to a Python ``float``
        object.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   zero-dimensional array instance. Must have a floating-point
                data type.
        
        
        Returns
        =======
        
        *   **out**: *<float>*
        
            *   a Python ``float`` object representing the single element of
                the array instance."""
        raise NotImplementedError

    def __floordiv__(self, other, /):
        """__floordiv__(self, other, /)
        ****************************
        
        Evaluates ``self_i // other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `floor_divide(x1, x2)
            <#floor-divide-x1-x2>`_."""
        raise NotImplementedError

    def __ge__(self, other, /):
        """__ge__(self, other, /)
        **********************
        
        Computes the truth value of ``self_i >= other_i`` for each element of
        an array instance with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type of ``bool``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `greater_equal(x1, x2)
            <#greater-equal-x1-x2>`_."""
        raise NotImplementedError

    def __getitem__(self, key, /):
        """__getitem__(self, key, /)
        *************************
        
        Returns ``self[key]``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance.
        
        *   **key**: *Union[ int, slice, ellipsis, Tuple[ Union[ int, slice,
            ellipsis ], … ], <array> ]*
        
            *   index key.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the accessed value(s). The returned array
                must have the same data type as ``self``."""
        raise NotImplementedError

    def __gt__(self, other, /):
        """__gt__(self, other, /)
        **********************
        
        Computes the truth value of ``self_i > other_i`` for each element of
        an array instance with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type of ``bool``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `greater(x1, x2)
            <#greater-x1-x2>`_."""
        raise NotImplementedError

    def __index__(self, /):
        """__index__(self, /)
        ******************
        
        Converts a zero-dimensional integer array to a Python ``int`` object.
        
        Note: This method is called to implement `operator.index()
            <https://docs.python.org/3/reference/datamodel.html#object.__index_\_>`_.
            See also `PEP 357 <https://www.python.org/dev/peps/pep-0357/>`_.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   zero-dimensional array instance. Must have an integer data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<int>*
        
            *   a Python ``int`` object representing the single element of the
                array instance."""
        raise NotImplementedError

    def __int__(self, /):
        """__int__(self, /)
        ****************
        
        Converts a zero-dimensional integer array to a Python ``int`` object.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   zero-dimensional array instance. Must have an integer data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<int>*
        
            *   a Python ``int`` object representing the single element of the
                array instance."""
        raise NotImplementedError

    def __invert__(self, /):
        """__invert__(self, /)
        *******************
        
        Evaluates ``~self_i`` for each element of an array instance.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have an integer or boolean data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have the same data type as ``self``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `bitwise_invert(x)
            <#bitwise-invert-x>`_."""
        raise NotImplementedError

    def __le__(self, other, /):
        """__le__(self, other, /)
        **********************
        
        Computes the truth value of ``self_i <= other_i`` for each element of
        an array instance with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type of ``bool``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `less_equal(x1, x2)
            <#less-equal-x1-x2>`_."""
        raise NotImplementedError

    def __len__(self, /):
        """__len__(self, /)
        ****************
        
        *TODO: need to more carefully consider this in order to accommodate,
        e.g., graph tensors where a shape may be dynamic. Furthermore, not
        clear whether this should be implemented, as, e.g., NumPy’s behavior
        of returning the size of the first dimension is not necessarily
        intuitive, as opposed to, say, the total number of elements.*"""
        raise NotImplementedError

    def __lshift__(self, other, /):
        """__lshift__(self, other, /)
        **************************
        
        Evaluates ``self_i << other_i`` for each element of an array instance
        with the respective element  of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have an integer data type.
        
        *   **other**: *Union[ int, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have an integer data
                type. Each element must be greater than or equal to ``0``.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have the same data type as ``self``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `bitwise_left_shift(x1, x2)
            <#bitwise-left-shift-x1-x2>`_."""
        raise NotImplementedError

    def __lt__(self, other, /):
        """__lt__(self, other, /)
        **********************
        
        Computes the truth value of ``self_i < other_i`` for each element of
        an array instance with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type of ``bool``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `less(x1, x2) <#less-x1-x2>`_."""
        raise NotImplementedError

    def __matmul__(self, other, /):
        """__matmul__(self, other, /)
        **************************
        
        Computes the matrix product.
        
        Note: The ``matmul`` function must implement the same semantics as the
            built-in ``@`` operator (see `PEP 465
            <https://www.python.org/dev/peps/pep-0465>`_).
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type. Must have at
                least one dimension. If ``self`` is one-dimensional having
                shape ``(M)`` and ``other`` has more than one dimension,
                ``self`` must be promoted to a two-dimensional array by
                prepending ``1`` to its dimensions (i.e., must have shape
                ``(1, M)``). After matrix multiplication, the prepended
                dimensions in the returned array must be removed. If ``self``
                has more than one dimension (including after vector-to-matrix
                promotion), ``self`` must be compatible with ``other`` (see
                `Broadcasting <#broadcasting>`_). If ``self`` has shape
                ``(..., M, K)``, the innermost two dimensions form matrices on
                which to perform matrix multiplication.
        
        *   **other**: *<array>*
        
            *   other array. Should have a numeric data type. Must have at
                least one dimension. If ``other`` is one-dimensional having
                shape ``(N)`` and ``self`` has more than one dimension,
                ``other`` must be promoted to a two-dimensional array by
                appending ``1`` to its dimensions (i.e., must have shape ``(N,
                1)``). After matrix multiplication, the appended dimensions in
                the returned array must be removed. If ``other`` has more than
                one dimension (including after vector-to-matrix promotion),
                ``other`` must be compatible with ``self`` (see `Broadcasting
                <#broadcasting>`_). If ``other`` has shape ``(..., K, N)``,
                the innermost two dimensions form matrices on which to perform
                matrix multiplication.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   if both ``self`` and ``other`` are one-dimensional arrays
                having shape ``(N)``, a zero-dimensional array containing the
                inner product as its only element.
        
            *   if ``self`` is a two-dimensional array having shape ``(M, K)``
                and ``other`` is a two-dimensional array having shape ``(K,
                N)``, a two-dimensional array containing the `conventional
                matrix product
                <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ and
                having shape ``(M, N)``.
        
            *   if ``self`` is a one-dimensional array having shape ``(K)``
                and ``other`` is an array having shape ``(..., K, N)``, an
                array having shape ``(..., N)`` (i.e., prepended dimensions
                during vector-to-matrix promotion must be removed) and
                containing the `conventional matrix product
                <https://en.wikipedia.org/wiki/Matrix_multiplication>`_.
        
            *   if ``self`` is an array having shape ``(..., M, K)`` and
                ``other`` is a one-dimensional array having shape ``(K)``, an
                array having shape ``(..., M)`` (i.e., appended dimensions
                during vector-to-matrix promotion must be removed) and
                containing the `conventional matrix product
                <https://en.wikipedia.org/wiki/Matrix_multiplication>`_.
        
            *   if ``self`` is a two-dimensional array having shape ``(M, K)``
                and ``other`` is an array having shape ``(..., K, N)``, an
                array having shape ``(..., M, N)`` and containing the
                `conventional matrix product
                <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ for
                each stacked matrix.
        
            *   if ``self`` is an array having shape ``(..., M, K)`` and
                ``other`` is a two-dimensional array having shape ``(K, N)``,
                an array having shape ``(..., M, N)`` and containing the
                `conventional matrix product
                <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ for
                each stacked matrix.
        
            *   if either ``self`` or ``other`` has more than two dimensions,
                an array having a shape determined by `Broadcasting
                <#broadcasting>`_ ``self`` against ``other`` and containing
                the `conventional matrix product
                <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ for
                each stacked matrix.
        
            The returned array must have a data type determined by `Type
            Promotion Rules <#type-promotion>`_.
        
            Note: Results must equal the results returned by the equivalent
                function `matmul(x1, x2) <#matmul-x1-x2>`_.
        
        
        Raises
        ======
        
        *   if either ``self`` or ``other`` is a zero-dimensional array.
        
        *   if ``self`` is a one-dimensional array having shape ``(N)``,
            ``other`` is a one-dimensional array having shape ``(M)``, and ``N
            != M``.
        
        *   if ``self`` is an array having shape ``(..., M, K)``, ``other`` is
            an array having shape ``(..., L, N)``, and ``K != L``."""
        raise NotImplementedError

    def __mod__(self, other, /):
        """__mod__(self, other, /)
        ***********************
        
        Evaluates ``self_i % other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. Each
                element-wise result must have the same sign as the respective
                element ``other_i``. The returned array must have a
                floating-point data type determined by `Type Promotion Rules
                <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `remainder(x1, x2)
            <#remainder-x1-x2>`_."""
        raise NotImplementedError

    def __mul__(self, other, /):
        """__mul__(self, other, /)
        ***********************
        
        Calculates the product for each element of an array instance with the
        respective element of the array ``other``.
        
        
        Special Cases
        =============
        
        For floating-point operands, let ``self`` equal ``x1`` and ``other``
        equal ``x2``.
        
        *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
        
        *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
            is either ``+0`` or ``-0``, the result is ``NaN``.
        
        *   If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either
            ``+infinity`` or ``-infinity``, the result is ``NaN``.
        
        *   If ``x1_i`` and ``x2_i`` have the same mathematical sign, the
            result has a positive mathematical sign, unless the result is
            ``NaN``. If the result is ``NaN``, the “sign” of ``NaN`` is
            implementation-defined.
        
        *   If ``x1_i`` and ``x2_i`` have different mathematical signs, the
            result has a negative mathematical sign, unless the result is
            ``NaN``. If the result is ``NaN``, the “sign” of ``NaN`` is
            implementation-defined.
        
        *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
            is either ``+infinity`` or ``-infinity``, the result is a signed
            infinity with the mathematical sign determined by the rule already
            stated above.
        
        *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
            is a nonzero finite number, the result is a signed infinity with
            the mathematical sign determined by the rule already stated above.
        
        *   If ``x1_i`` is a nonzero finite number and ``x2_i`` is either
            ``+infinity`` or ``-infinity``, the result is a signed infinity
            with the mathematical sign determined by the rule already stated
            above.
        
        *   In the remaining cases, where neither ``infinity`` nor ``NaN`` is
            involved, the product must be computed and rounded to the nearest
            representable value according to IEEE 754-2019 and a supported
            rounding mode. If the magnitude is too large to represent, the
            result is an ``infinity`` of appropriate mathematical sign. If the
            magnitude is too small to represent, the result is a zero of
            appropriate mathematical sign.
        
        Note: Floating-point multiplication is not always associative due to
            finite precision.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise products. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `multiply(x1, x2)
            <#multiply-x1-x2>`_."""
        raise NotImplementedError

    def __ne__(self, other, /):
        """__ne__(self, other, /)
        **********************
        
        Computes the truth value of ``self_i != other_i`` for each element of
        an array instance with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. May have any data type.
        
        *   **other**: *Union[ int, float, bool, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). May have any data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type of ``bool`` (i.e., must be a
                boolean array).
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `not_equal(x1, x2)
            <#not-equal-x1-x2>`_."""
        raise NotImplementedError

    def __neg__(self, /):
        """__neg__(self, /)
        ****************
        
        Evaluates ``-self_i`` for each element of an array instance.
        
        Note: For signed integer data types, the numerical negative of the
            minimum representable integer is implementation-dependent.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the evaluated result for each element in
                ``self``. The returned array must have a data type determined
                by `Type Promotion Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `negative(x) <#negative-x>`_."""
        raise NotImplementedError

    def __or__(self, other, /):
        """__or__(self, other, /)
        **********************
        
        Evaluates ``self_i | other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have an integer or boolean data type.
        
        *   **other**: *Union[ int, bool, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have an integer or
                boolean data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `bitwise_or(x1, x2)
            <#bitwise-or-x1-x2>`_."""
        raise NotImplementedError

    def __pos__(self, /):
        """__pos__(self, /)
        ****************
        
        Evaluates ``+self_i`` for each element of an array instance.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the evaluated result for each element. The
                returned array must have the same data type as ``self``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `positive(x) <#positive-x>`_."""
        raise NotImplementedError

    def __pow__(self, other, /):
        """__pow__(self, other, /)
        ***********************
        
        Calculates an implementation-dependent approximation of exponentiation
        by raising each element (the base) of an array instance to the power
        of ``other_i`` (the exponent), where ``other_i`` is the corresponding
        element of the array ``other``.
        
        
        Special Cases
        =============
        
        For floating-point operands, let ``self`` equal ``x1`` and ``other``
        equal ``x2``.
        
        *   If ``x1_i`` is not equal to ``1`` and ``x2_i`` is ``NaN``, the
            result is ``NaN``.
        
        *   If ``x2_i`` is ``+0``, the result is ``1``, even if ``x1_i`` is
            ``NaN``.
        
        *   If ``x2_i`` is ``-0``, the result is ``1``, even if ``x1_i`` is
            ``NaN``.
        
        *   If ``x1_i`` is ``NaN`` and ``x2_i`` is not equal to ``0``, the
            result is ``NaN``.
        
        *   If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is
            ``+infinity``, the result is ``+infinity``.
        
        *   If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is
            ``-infinity``, the result is ``+0``.
        
        *   If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``+infinity``, the
            result is ``1``.
        
        *   If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``-infinity``, the
            result is ``1``.
        
        *   If ``x1_i`` is ``1`` and ``x2_i`` is not ``NaN``, the result is
            ``1``.
        
        *   If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``+infinity``,
            the result is ``+0``.
        
        *   If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``-infinity``,
            the result is ``+infinity``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is greater than ``0``,
            the result is ``+infinity``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is less than ``0``, the
            result is ``+0``.
        
        *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is greater than ``0``,
            the result is ``-infinity``.
        
        *   If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and
            ``x2_i`` is not an odd integer value, the result is ``+infinity``.
        
        *   If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and
            ``x2_i`` is an odd integer value, the result is ``-0``.
        
        *   If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and
            ``x2_i`` is not an odd integer value, the result is ``+0``.
        
        *   If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the
            result is ``+0``.
        
        *   If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result
            is ``+infinity``.
        
        *   If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and
            ``x2_i`` is an odd integer value, the result is ``-0``.
        
        *   If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and
            ``x2_i`` is not an odd integer value, the result is ``+0``.
        
        *   If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i``
            is an odd integer value, the result is ``-infinity``.
        
        *   If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i``
            is not an odd integer value, the result is ``+infinity``.
        
        *   If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number,
            ``x2_i`` is a finite number, and ``x2_i`` is not an integer value,
            the result is ``NaN``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance whose elements correspond to the exponentiation
                base. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array whose elements correspond to the exponentiation
                exponent. Must be compatible with ``self`` (see `Broadcasting
                <#broadcasting>`_). Should have a numeric data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `pow(x1, x2) <#pow-x1-x2>`_."""
        raise NotImplementedError

    def __rshift__(self, other, /):
        """__rshift__(self, other, /)
        **************************
        
        Evaluates ``self_i >> other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have an integer data type.
        
        *   **other**: *Union[ int, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have an integer data
                type. Each element must be greater than or equal to ``0``.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have the same data type as ``self``.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `bitwise_right_shift(x1, x2)
            <#bitwise-right-shift-x1-x2>`_."""
        raise NotImplementedError

    def __setitem__(self, key, value, /):
        """__setitem__(self, key, value, /)
        ********************************
        
        Sets ``self[key]`` to ``value``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance.
        
        *   **key**: *Union[ int, slice, ellipsis, Tuple[ Union[ int, slice,
            ellipsis ], … ], <array> ]*
        
            *   index key.
        
        *   **value**: *Union[ int, float, bool, <array> ]*
        
            *   value(s) to set. Must be compatible with ``self[key]`` (see
                `Broadcasting <#broadcasting>`_).
        
        Note: Setting array values must not affect the data type of
            ``self``.When ``value`` is a Python scalar (i.e., ``int``,
            ``float``, ``bool``), behavior must follow specification guidance
            on mixing arrays with Python scalars (see `Type Promotion Rules
            <#type-promotion>`_).When ``value`` is an ``array`` of a different
            data type than ``self``, how values are cast to the data type of
            ``self`` is implementation defined."""
        raise NotImplementedError

    def __sub__(self, other, /):
        """__sub__(self, other, /)
        ***********************
        
        Calculates the difference for each element of an array instance with
        the respective element of the array ``other``. The result of ``self_i
        - other_i`` must be the same as ``self_i + (-other_i)`` and must be
        governed by the same floating-point rules as addition (see `__add__()
        <add-self-other_>`_).
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance (minuend array). Should have a numeric data
                type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   subtrahend array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise differences. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `subtract(x1, x2)
            <#subtract-x1-x2>`_."""
        raise NotImplementedError

    def __truediv__(self, other, /):
        """__truediv__(self, other, /)
        ***************************
        
        Evaluates ``self_i / other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Special Cases
        =============
        
        For floating-point operands, let ``self`` equal ``x1`` and ``other``
        equal ``x2``.
        
        *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
        
        *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
            is either ``+infinity`` or ``-infinity``, the result is ``NaN``.
        
        *   If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either
            ``+0`` or ``-0``, the result is ``NaN``.
        
        *   If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the
            result is ``+0``.
        
        *   If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the
            result ``-0``.
        
        *   If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result
            is ``-0``.
        
        *   If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result
            is ``+0``.
        
        *   If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the
            result is ``+infinity``.
        
        *   If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the
            result is ``-infinity``.
        
        *   If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result
            is ``-infinity``.
        
        *   If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result
            is ``+infinity``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is a positive (i.e.,
            greater than ``0``) finite number, the result is ``+infinity``.
        
        *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is a negative (i.e.,
            less than ``0``) finite number, the result is ``-infinity``.
        
        *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is a positive (i.e.,
            greater than ``0``) finite number, the result is ``-infinity``.
        
        *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is a negative (i.e.,
            less than ``0``) finite number, the result is ``+infinity``.
        
        *   If ``x1_i`` is a positive (i.e., greater than ``0``) finite number
            and ``x2_i`` is ``+infinity``, the result is ``+0``.
        
        *   If ``x1_i`` is a positive (i.e., greater than ``0``) finite number
            and ``x2_i`` is ``-infinity``, the result is ``-0``.
        
        *   If ``x1_i`` is a negative (i.e., less than ``0``) finite number
            and ``x2_i`` is ``+infinity``, the result is ``-0``.
        
        *   If ``x1_i`` is a negative (i.e., less than ``0``) finite number
            and ``x2_i`` is ``-infinity``, the result is ``+0``.
        
        *   If ``x1_i`` and ``x2_i`` have the same mathematical sign and are
            both nonzero finite numbers, the result has a positive
            mathematical sign.
        
        *   If ``x1_i`` and ``x2_i`` have different mathematical signs and are
            both nonzero finite numbers, the result has a negative
            mathematical sign.
        
        *   In the remaining cases, where neither ``-infinity``, ``+0``,
            ``-0``, nor ``NaN`` is involved, the quotient must be computed and
            rounded to the nearest representable value according to IEEE
            754-2019 and a supported rounding mode. If the magnitude is too
            larger to represent, the operation overflows and the result is an
            ``infinity`` of appropriate mathematical sign. If the magnitude is
            too small to represent, the operation underflows and the result is
            a zero of appropriate mathematical sign.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have a numeric data type.
        
        *   **other**: *Union[ int, float, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have a numeric data
                type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `divide(x1, x2)
            <#divide-x1-x2>`_."""
        raise NotImplementedError

    def __xor__(self, other, /):
        """__xor__(self, other, /)
        ***********************
        
        Evaluates ``self_i ^ other_i`` for each element of an array instance
        with the respective element of the array ``other``.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance. Should have an integer or boolean data type.
        
        *   **other**: *Union[ int, bool, <array> ]*
        
            *   other array. Must be compatible with ``self`` (see
                `Broadcasting <#broadcasting>`_). Should have an integer or
                boolean data type.
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array containing the element-wise results. The returned
                array must have a data type determined by `Type Promotion
                Rules <#type-promotion>`_.
        
        Note: Element-wise results must equal the results returned by the
            equivalent element-wise function `bitwise_xor(x1, x2)
            <#bitwise-xor-x1-x2>`_."""
        raise NotImplementedError

    def to_device(self, device, /):
        """to_device(self, device, /)
        **************************
        
        Move the array to the given device.
        
        
        Parameters
        ==========
        
        *   **self**: *<array>*
        
            *   array instance.
        
        *   **device**: *<device>*
        
            *   a ``device`` object (see device-support).
        
        
        Returns
        =======
        
        *   **out**: *<array>*
        
            *   an array with the same data and dtype, located on the
                specified device."""
        raise NotImplementedError

