odds = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        odds.append(n)
if odds:
    print(sum(odds), min(odds), sep='\n')
else:
    print(-1)