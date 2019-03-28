#
# a = [2,6,3,7]
# b = [3,2,1,7]
# c = 0
# c1 = 0
# c2 = 0
# for i in range(len(a)):
#     x = a[i]
#
#     y = b[i]
#     if x > y:
#         c1 += 1
#     elif x < y:
#         c2 += 1
#     else:
#         c = 0
# print(c1,c2)
#
# matrix = [[11,2 ,4,
#             4 ,5,6,
#             10 ,8 ,-12]]
# l= len(matrix[0])
# r1 = [matrix[i][i] for i in range(l)]
# r2 = [matrix[l-1-i][i] for i in range(l-1, -1, -1)]
# r = sum(r1) - sum(r2)
# print (r1, r2, r)
#


l1 = [1,2,3,4]
l2 = [12,3,4,6]
d = dict(zip(l1,l2))
print (d)
print (d.keys(),d.values(),d.items(),d.viewitems(),d.viewkeys(),d.viewvalues())
print (d.iteritems())
d2 = d.copy()
print (d2, id(d2))
d3 =d2
print (d3)
#
#
#
#
#
