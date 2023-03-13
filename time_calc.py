from math import exp, sin
import time

def calculate(a):
    result = 0
    for val in a:
        result += exp(val) * sin(val)
    return result

x = [0.1 * i for i in range(1000)]
t0 = time.process_time()
for r in range(1000):
    calculate(x)
t1 = time.process_time()
print("Time spent", t1 - t0)
