n = int(input())
nums = list(map(int, input().split()))

count = 0
for num in nums:
    if num == 1:
        continue
    prime = True
    for j in range(2, num):
        if num % j == 0:
            prime = False
            break
    if prime:
        count += 1
print(count)