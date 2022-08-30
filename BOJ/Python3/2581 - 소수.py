from math import sqrt, floor
m = int(input())
n = int(input())
sum, min = 0, 0
for i in range(m,n+1):
    err = 0
    for j in range(2,floor(sqrt(i))+1):
        if i % j == 0:
            err += 1
            break
    if err == 0 and i != 1:
        if sum == 0:
            min = i
        sum += i
if sum == 0:
    print(-1)
else:
    print(sum, min, sep='\n')