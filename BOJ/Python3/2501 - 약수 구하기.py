n, k = map(int, input().split())
count, divisor = 0, 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
    if count == k:
        divisor = i
        break
print(divisor)