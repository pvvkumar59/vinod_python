# arr = [-4,3,-9,0,4,1]
# l = len(arr)
# p = 0
# n = 0
# z = 0
# for i in range(l):
#     if arr[i] > 0:
#         p += 1
#     elif arr[i] < 0:
#         n += 1
#     elif arr[i] == 0:
#         z += 1
# le = float(l)
# pf = p/le
# nf = n/le
# zf = z/le
#
# pff = format(pf,'.6f')
# nff = format(nf,'.6f')
# zff = format(zf,'.6f')
#
# print (pff)
#
#
#

# Complete the plusMinus function below.


def plusMinus(arr):

    l = len(arr)
    p = 0
    n = 0
    z = 0
    for i in range(l):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        elif arr[i] == 0:
            z += 1

    le = float(l)
    pf = p / le
    nf = n / le
    zf = z / le
    pff = format(pf, '.6f')
    nff = format(nf, '.6f')
    zff = format(zf, '.6f')

    print (pff)

    return pff, nff, zff


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    op = plusMinus(arr)
    print (op)