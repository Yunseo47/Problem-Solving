n = int(input())
for i in range(n,1,-1):
    str = ' '*(n-i) + '*'*(2*i-1)
    print(str)
for i in range(1,n+1):
    str = ' '*(n-i) + '*'*(2*i-1)
    print(str)