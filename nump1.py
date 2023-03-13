import numpy

x = numpy.array((1, 2, 3, 4))
print(x)
y = numpy.array((1, 2, 3, 4), float)
print(y)

# output: [ 1.  2.  3.  4.]
data = [[1, 2, 3], [4, 5, 6]]
z = numpy.array(data, complex)

print(z)
# output: [[ 1.+0.j  2.+0.j  3.+0.j]
#          [ 4.+0.j  5.+0.j  6.+0.j]]

print(z.shape)
# output: (2, 3)

print(z.size)

a = numpy.arange(10)

print(a)
# output: [0 1 2 3 4 5 6 7 8 9]

b = numpy.linspace(-4.5, 4.5, 5)

print(b)
# output: [-4.5  -2.25  0.    2.25  4.5]

c = numpy.zeros((4, 6), float)
d = numpy.ones((2, 4))
e = numpy.full((3, 2), 4.2)

print(c.shape)
print(d)
print(e)
# output:
#   (4, 6)
#   [[ 1.  1.  1.  1.]
#    [ 1.  1.  1.  1.]]
#   [[4.2 4.2]
#    [4.2 4.2]
#    [4.2 4.2]]

s = numpy.array(['foo', 'foo-bar'])

print(repr(s))
# output: array(['foo', 'foo-bar'],
#               dtype='|U7')

dna = 'AAAGTCTGAC'
c = numpy.array(dna, dtype='c')

print(repr(c))
# output:
#   array([b'A', b'A', b'A', b'G', b'T', b'C', b'T', b'G', b'A', b'C'],
#         dtype='|S1')

data = numpy.array([[1, 2, 3], [4, 5, 6]])
x = data[0,2]
y = data[1,-2]

print(x, y)
# output: 3 5

a = numpy.arange(10)

print(a[2:])
# output: [2 3 4 5 6 7 8 9]

print(a[:-1])
# output: [0 1 2 3 4 5 6 7 8]

print(a[1:7:2])
# output: [1 3 5]


a = numpy.arange(10)
a[1:3] = -1

b = numpy.zeros((4, 4))
b[1:3, 1:3] = 2.0

print(a)
print(b)
# output:
#   [ 0 -1 -1  3  4  5  6  7  8  9]
#   [[ 0.  0.  0.  0.]
#    [ 0.  2.  2.  0.]
#    [ 0.  2.  2.  0.]
#    [ 0.  0.  0.  0.]]


a = numpy.arange(10)
b = a              # reference, changing values in b changes a
b = a.copy()       # true copy


a = numpy.arange(10)
c = a[1:4]         # view, changing c changes elements [1:4] of a
c = a[1:4].copy()  # true copy of subarray
