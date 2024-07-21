n = int(input())
rst = 'false'
if (n % 2 == 1 and n % 3 == 0) or (n % 2 == 0 and n % 5 == 0) :
    rst = 'true'

print(rst)