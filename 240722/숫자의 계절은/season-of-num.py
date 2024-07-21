m = int(input())
rst = 'Winter'

if m <= 2 :
    rst = 'Winter'
elif m <= 5 :
    rst = 'Spring'
elif m <= 8 :
    rst = 'Summer'
elif m <= 11 :
    rst = 'Fall'

print(rst)