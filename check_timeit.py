from math import sin, cos
import timeit

tyme = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tyme)
