n = int(input())
for i in range(1, n):
    str = '*'*i + ' '*2*(n-i) + '*'*i
    print(str)
for i in range(n, 0, -1):
    str = '*'*i + ' '*2*(n-i) + '*'*i
    print(str)