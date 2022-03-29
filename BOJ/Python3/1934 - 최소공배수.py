from sys import stdin
input = stdin.readline

def gcd(m, n):  # 반복문으로 구현하였다. 재귀함수를 이용해서도 구현 가능하다.
    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m%n
    return n
    
def lcm(m, n):
    return m * n // gcd(m, n)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))