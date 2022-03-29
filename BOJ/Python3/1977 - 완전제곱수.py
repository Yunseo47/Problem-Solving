m = int(input())
n = int(input())
sqr = [i*i for i in range(101) if m<=i*i<=n]  # 'i**2'보다 'i*i'가 실행속도가 더 빠르다.
print(str(sum(sqr))+'\n'+str(sqr[0]) if sqr else -1)