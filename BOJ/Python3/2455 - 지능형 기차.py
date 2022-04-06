count = [0 for i in range(4)]
for i in range(4):
    m, p = map(int, input().split())
    count[i] = count[i-1] - m + p
print(max(count))