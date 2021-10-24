bool = NotImplemented
"""
bool
****

Boolean (``True`` or ``False``).
"""

int8 = NotImplemented
"""
int8
****

An 8-bit signed integer whose values exist on the interval ``[-128,
+127]``.
"""

int16 = NotImplemented
"""
int16
*****

A 16-bit signed integer whose values exist on the interval ``[−32,767,
+32,767]``.
"""

int32 = NotImplemented
"""
int32
*****

A 32-bit signed integer whose values exist on the interval
``[−2,147,483,647, +2,147,483,647]``.
"""

int64 = NotImplemented
"""
int64
*****

A 64-bit signed integer whose values exist on the interval
``[−9,223,372,036,854,775,807, +9,223,372,036,854,775,807]``.
"""

uint8 = NotImplemented
"""
uint8
*****

An 8-bit unsigned integer whose values exist on the interval ``[0,
+255]``.
"""

uint16 = NotImplemented
"""
uint16
******

A 16-bit unsigned integer whose values exist on the interval ``[0,
+65,535]``.
"""

uint32 = NotImplemented
"""
uint32
******

A 32-bit unsigned integer whose values exist on the interval ``[0,
+4,294,967,295]``.
"""

uint64 = NotImplemented
"""
uint64
******

A 64-bit unsigned integer whose values exist on the interval ``[0,
+18,446,744,073,709,551,615]``.
"""

float32 = NotImplemented
"""
float32
*******

IEEE 754 single-precision (32-bit) binary floating-point number (see
IEEE 754-2019).
"""

float64 = NotImplemented
"""
float64
*******

IEEE 754 double-precision (64-bit) binary floating-point number (see
IEEE 754-2019).

Future extension: ``complex64`` and ``complex128`` dtypes are expected
to be included in the next version of this standard and to have the
following casting rules (will be added to `Type Promotion Rules
<#type-promotion>`_):

.. image:: _static/images/dtype_promotion_complex.png

See `array-api/issues/102
<https://github.com/data-apis/array-api/issues/102>`_ for more
details.

Note: A conforming implementation of the array API standard may provide
    and support additional data types beyond those described in this
    specification.
"""

