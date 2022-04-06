from sys import stdin
input = stdin.readline

def reward(a,b,c):
    if a == b and b == c:  # 같은 눈 3개
        return 10000 + a*1000
    elif a == b or b == c or c == a:  # 같은 눈 2개
        return 1000 + (sum((a,b,c))-(a^b^c))*50  # XOR 연산 a^b^c 수행 시 셋 중 다른 눈의 값 얻음
    else:  # 모두 다른 눈
        return max(a,b,c)*100
            
n = int(input())
prize = 0
for i in range(n):
    a, b, c = map(int, input().split())
    prize = max(prize, reward(a,b,c))
print(prize)