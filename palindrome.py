# # def extendlist(val, list=[]):
# #     list.append(val)
# #     return list
# #
# # list1 = extendlist(10)
# # list2 = extendlist(123, [])
# # list3 = extendlist('a')
# # print(list1, list2, list3)
#
# # import re
# # e = re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','ayushiwashere@gmail.com')
# # e.group()
# # print(e.group())
#
# str = "vinod python"
# print(str.isalnum(), str.isalnum(), str.isupper(), str.islower(), str.isdigit())
# l = [1,3,6,9]
# l.reverse()
# l[3] = [1,2,3]
# l[2][2] = 10
# print (l)

num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ',num_array