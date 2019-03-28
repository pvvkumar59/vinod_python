#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    n = len(arr)
    r1 = sum([arr[i][i] for i in range(n)])
    r2 = sum([arr[n - 1 - i][i] for i in range(n - 1, -1, -1)])

    result = abs(r1 - r2)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
