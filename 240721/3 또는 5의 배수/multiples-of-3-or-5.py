a = int(input())
rst1 = 'NO'
rst2 = 'NO'

if a % 3 == 0 :
    rst1 = 'YES'
if a % 5 == 0 :
    rst2 = 'YES'

print(f"{rst1}\n{rst2}")