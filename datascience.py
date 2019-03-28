# # import numpy as np
# #
# # print(np.eye(3))
# # # print(a)
# #
# n = [10,11,12]
# def fun(x):
#     x[0] = 5
#     return x
#
# print(n)
# print(fun(n),n)

# print(max("what are you"))
# a=10
# b=20
# def change():
#     global b
#     a=45
#     b=56
# change()
# # print(a)
# # # print(b)

# a =[1,2,3,4,5]
# b= lambda x:(b(x[1:]) + x[:1] if x else[])
# print(b(a))
# a =[1,2,3]
# b=a.append(4)
# print(a)
# print(b)
#
# example = "snowworld"
# print ("%s" % example[4:7])
# names = ['r','t']
# print("\n".join(names))

# d = {"k":4}
# print(d["l"])
#
# print(ord(65))
# print(ord('A'))

# B=[1,5,3,8]
# print(x[rev(ord(x$B))])
# print(ordersort)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)
ls = [1,"vinod","2.4"]
print(ls)
tu = (1,"te","1.44")
print(tu)