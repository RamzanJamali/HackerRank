
from ast import And
from cmath import sqrt
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    x = int(first_multiple_input[0])

    y = int(first_multiple_input[1])

    disti = abs(sqrt((x * x) + (y * y)))

    sum_points = [disti]
    dis_points = [(x, y)]

    x_range = range(-12,12,1)
    y_range = range(-12,12,1)
    breaker = False

    for xx in x_range:
        for yy in y_range:
            if xx == x and yy == y:
                continue
            origin_dis = abs(sqrt(xx * xx + yy * yy))
            if abs(origin_dis - round(origin_dis)) < 0.00000000001 :
                victor = False

            else:
                victor = True
                    
            if victor is True:   
                sum_points.append(origin_dis)
                dis_points.append((xx, yy))
                print(xx, yy)
                #print(origin_dis)
            else:
                continue

            if len(sum_points) == 12:
                total_distance = sum(sum_points)
                print(total_distance)
                #nearest_integer = round(total_distance)
                breaker = True
                break
        if breaker is True:
            break






