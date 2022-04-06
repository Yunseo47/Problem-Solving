def draw(n):  # 재귀함수로 구현하였다. 반복문을 사용할 수도 있다.
    if n == 3:
        Z = ['  *  ',' * * ','*****']
        return Z
    
    else:
        Z = draw(n//2)
        
        X = [' '*(n//2) + i + ' '*(n//2) for i in Z]
        Y = [i + ' ' + i for i in Z]

        Z = X + Y
        return Z

n = int(input())
print('\n'.join(draw(n)))