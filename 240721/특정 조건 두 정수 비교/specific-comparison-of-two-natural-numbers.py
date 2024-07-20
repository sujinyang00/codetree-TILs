a, b = map(int, input().split())
r1, r2 = 0, 0

if a < b :
    r1 = 1
elif a == b :    
    r2 = 1

print(r1, r2, end=" ")