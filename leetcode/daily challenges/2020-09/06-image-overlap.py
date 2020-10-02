import numpy

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        padded = numpy.zeros((len(A) + len(A)-1, len(A) + len(A)-1), dtype=int)
        padded[len(A)//2:len(A)+len(A)//2, len(A)//2:len(A)+len(A)//2] = A
        return conv2d(padded, numpy.asarray(B)).max()
    
    
def conv2d(a, f):
    s = f.shape + tuple(numpy.subtract(a.shape, f.shape) + 1)
    strd = numpy.lib.stride_tricks.as_strided
    subM = strd(a, shape = s, strides = a.strides * 2)
    return numpy.einsum('ij,ijkl->kl', f, subM)