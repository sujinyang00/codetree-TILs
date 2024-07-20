a, b, c = map(int, input().split())
rst1 = 0
rst2 = 0
if a == min(a, b, c) :
    rst1 = 1
if a == b and b == c :
    rst2 = 1

print(rst1, rst2)