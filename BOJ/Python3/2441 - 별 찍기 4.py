n = int(input())
for i in range(n,0,-1):
    str = '*'*i
    print(str.rjust(n))