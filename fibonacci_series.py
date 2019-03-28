n = 10
n1 = 0
n2 = 1
i = 0

# using for loop
for x in range(n):
    print(n1)
    i = n1+n2
    n1 = n2
    n2 = i
    i = i+1
# # using while loop
while i < n:
    print(n1)
    nth =n1+n2
    n1=n2
    n2 = nth
    i=i+1
