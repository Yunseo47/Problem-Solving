n = int(input())
marks = list(map(int, input().split()))
count, score = 0, 0
for mark in marks:
    if mark == 0:
        count = 0
    else:
        count += 1
        score += count
print(score)