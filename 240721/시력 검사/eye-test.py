a = float(input())
b = float(input())
rst = 'Low'
if a >= 1.0 and b >= 1.0 :
    rst = 'High'
elif a >= 0.5 and b >= 0.5 :
    rst = 'Middle'

print(rst)