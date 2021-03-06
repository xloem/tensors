# from https://github.com/vadimkantorov/pydlpack/blob/60edf35397b4f3964dbb82723052e30b45b67623/dlpack.py

import ctypes

class DLDeviceType(ctypes.c_int):
	kDLCPU = 1
	kDLGPU = 2
	kDLCPUPinned = 3
	kDLOpenCL = 4
	kDLVulkan = 7
	kDLMetal = 8
	kDLVPI = 9
	kDLROCM = 10
	kDLExtDev = 12

class DLDataTypeCode(ctypes.c_uint8):
	kDLInt = 0
	kDLUInt = 1
	kDLFloat = 2
	kDLBfloat = 4

	def __str__(self):
		return {self.kDLInt : 'int', self.kDLUInt : 'uint', self.kDLFloat : 'float', self.kDLBfloat : 'bfloat'}[self.value]

class DLDataType(ctypes.Structure):
	_fields_ = [
		('type_code', DLDataTypeCode),
		('bits', ctypes.c_uint8),
		('lanes', ctypes.c_uint16)
	]

	@property
	def descr(self):
		typestr = str(self.type_code) + str(self.bits)
		return [('f' + str(l), typestr) for l in range(self.lanes)]
	
	def __str__(self):
		return repr(self.descr)

class DLContext(ctypes.Structure):
	_fields_ = [
		('device_type', DLDeviceType),
		('device_id', ctypes.c_int)
	]

class DLTensor(ctypes.Structure):
	_fields_ = [
		('data', ctypes.c_void_p),
		('ctx', DLContext),
		('ndim', ctypes.c_int),
		('dtype', DLDataType),
		('shape', ctypes.POINTER(ctypes.c_int64)),
		('strides', ctypes.POINTER(ctypes.c_int64)),
		('byte_offset', ctypes.c_uint64)
	]

	@property
	def size(self):
		prod = 1
		for i in range(self.ndim):
			prod *= self.shape[i]
		return prod

	@property
	def itemsize(self):
		return self.dtype.lanes * self.dtype.bits // 8;

	@property
	def nbytes(self):
		return self.size * self.itemsize 

	@property
	def __array_interface__(self):
		shape = tuple(self.shape[dim] for dim in range(self.ndim))
		strides = tuple(self.strides[dim] * self.itemsize for dim in range(self.ndim))
		typestr = '|' + str(self.dtype.type_code)[0] + str(self.itemsize)
		return dict(version = 3, shape = shape, strides = strides, data = (self.data, True), offset = self.byte_offset, typestr = typestr)
	
	def __str__(self):
		return 'dtype={dtype}, ndim={ndim}, shape={shape}, strides={strides}, byte_offset={byte_offset}'.format(dtype = self.dtype, ndim = self.ndim, shape = tuple(self.shape[i] for i in range(self.ndim)), strides = tuple(self.strides[i] for i in range(self.ndim)), byte_offset = self.byte_offset)

class DLManagedTensor(ctypes.Structure):
	_fields_ = [
		('dl_tensor', DLTensor),
		('manager_ctx', ctypes.c_void_p),
		('deleter', ctypes.CFUNCTYPE(None, ctypes.c_void_p))
	]

PyCapsule_Destructor = ctypes.CFUNCTYPE(None, ctypes.py_object)
PyCapsule_New = ctypes.pythonapi.PyCapsule_New
PyCapsule_New.restype = ctypes.py_object
PyCapsule_New.argtypes = (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)
PyCapsule_GetPointer = ctypes.pythonapi.PyCapsule_GetPointer
PyCapsule_GetPointer.restype = ctypes.c_void_p
PyCapsule_GetPointer.argtypes = (ctypes.py_object, ctypes.c_char_p)

def to_dlpack(dl_managed_tensor):
	return PyCapsule_New(ctypes.byref(dl_managed_tensor), b'dltensor', None)
		
def numpy_from_dlpack(pycapsule):
	dl_managed_tensor = ctypes.cast(PyCapsule_GetPointer(pycapsule, b'dltensor'), ctypes.POINTER(DLManagedTensor)).contents
	wrapped = type('', (), dict(__array_interface__ = dl_managed_tensor.dl_tensor.__array_interface__, __del__ = lambda self: dl_managed_tensor.deleter(ctypes.byref(dl_managed_tensor))))()
	return numpy.asarray(wrapped)
	
if __name__ == '__main__':
	import os
	import sys
	import numpy
	import torch.utils.dlpack
	
	lib = ctypes.CDLL(os.path.abspath('libdlpack.so'))
	lib.create_and_allocate_dlpack_tensor.restype = DLManagedTensor
	dl_managed_tensor = lib.create_and_allocate_dlpack_tensor()
	
	dlpack_tensor = to_dlpack(dl_managed_tensor)

	if 'numpy' in sys.argv[1]:
		array = numpy_from_dlpack(dlpack_tensor)
	elif 'torch' in sys.argv[1]:
		array = torch.utils.dlpack.from_dlpack(dlpack_tensor)
	
	array.tofile(sys.argv[1])
	del dlpack_tensor
