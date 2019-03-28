# # program to print prime numbers btwn 1 and 100
n = 100
p = []
np = []
for n in range(2, n+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                np.append(n)
                break
        else:
            p.append(n)
print(p)
print(np)
# ############# method 2 ##########
# ''' for a in range(2,r+1):
#     k=0
#     for i in range(2,a//2+1):
#         if(a%i==0):
#             k=k+1
#     if(k<=0):
#         print(a)  '''

arr = [1,3,5]
k = 5
for i in range(len(arr)):
    if arr[i] == k:
        print ("Yes")
    else:
        print("No")