def draw(n):  # 재귀함수로 구현하였다. 반복문을 사용할 수도 있다.
    if n == 3:
        Z = ['***','* *','***']
        return Z
    
    else:
        Z = draw(n//3)
        
        X = [i*3 for i in Z]
        Y = [i + ' '*(n//3) + i for i in Z]

        Z = X + Y + X
        return Z

n = int(input())
print('\n'.join(draw(n)))