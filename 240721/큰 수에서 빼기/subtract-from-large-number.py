a, b = map(int, input().split())
# a < b | a > b | a = b
if a >= b :
    print(a - b)
else :
    print(b - a)