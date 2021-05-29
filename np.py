import numpy
nm=input().split()
n,m=int(nm[0]),int(nm[1])
l=[input().spilt() for i in range(n)]
arr=numpy.array(l,int)
print(numpy.transpose(arr))
print(arr.faltten())
