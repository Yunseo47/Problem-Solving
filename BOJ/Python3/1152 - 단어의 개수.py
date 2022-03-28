import sys
s = sys.stdin.read().strip()
print(s.count(' ') + 1 if s else 0)