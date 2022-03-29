from sys import stdin

n = int(stdin.readline())
strips = list(map(int, stdin.read().split()))
print(sum(strips) - len(strips) + 1)

# 리스트 대신 반복문으로 구현할 수도 있다. 메모리를 적게 사용하는 대신, 실행 시간이 증가한다.