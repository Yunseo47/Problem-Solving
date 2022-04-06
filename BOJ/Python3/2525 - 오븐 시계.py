a, b = map(int, input().split())
c = int(input())
b += c
a += b//60
if a>23:
    a -= 24
b = b%60
print(a, b)