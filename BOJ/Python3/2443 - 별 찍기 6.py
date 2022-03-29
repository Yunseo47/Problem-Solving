n = int(input())
for i in range(n,0,-1):
    str = ' '*(n-i) + '*'*(2*i-1)
    print(str)