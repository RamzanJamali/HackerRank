#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ltr = []
    rtl = []
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                ltr.append(arr[i][j])
    for k in range(n):
        for l in range(n):
            if k == l:
                rtl.append(arr[k][n-k-1])

    l_sum = sum(ltr)
    r_sum = sum(rtl)
    print(abs(l_sum-r_sum))

if __name__ == '__main__':
    arr = [[1, 2, 3, 2],[4, 5, 5, 4],[ 7, 9, 9, 7], [1, 0, 0, 0]]
    diagonalDifference(arr)
