a,b,c = map(int, input().split())

if a == b and b == c:  # 같은 눈 3개
    print(10000 + a*1000)
elif a == b or b == c or c == a:  # 같은 눈 2개
    print(1000 + (sum((a,b,c))-(a^b^c))*50)  # XOR 연산 a^b^c 수행 시 셋 중 다른 눈의 값 얻음
else:  # 모두 다른 눈
    print(max(a,b,c)*100)