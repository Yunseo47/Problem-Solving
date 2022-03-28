word, c = input().upper(), []
for i in range(65,91):
    c.append(word.count(chr(i)))
print('?' if c.count(max(c))>1 else chr(c.index(max(c))+65))