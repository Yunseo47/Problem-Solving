max = 0
for i in range(9):
    num = int(input())
    if num > max:
        max = num
        index = i + 1
print(max)
print(index)

# max() 함수와 index() 메서드를 사용해 구현할 수도 있다.