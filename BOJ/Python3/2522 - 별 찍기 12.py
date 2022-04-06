n = int(input())
for i in range(1,n):
    str = '*'*i
    print(str.rjust(n))
for i in range(n,0,-1):
    str = '*'*i
    print(str.rjust(n))