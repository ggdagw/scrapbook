import ctypes
import numpy

from numpy.ctypeslib import ndpointer
lib = ctypes.cdll.LoadLibrary("./ctest.so")
fun = lib.cfun
fun.restype = None
fun.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ctypes.c_size_t,
                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]

# try it
indata = numpy.ones((5,6))
outdata = numpy.empty((5,6))

print(indata)
fun(indata, indata.size, outdata)
print(outdata)
