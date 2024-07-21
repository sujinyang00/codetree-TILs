m, f = map(int, input().split())
rst = 0

if m < 90 :
    rst = 0
# 아래로는 m >= 90인 값들
elif f >= 95 : 
    rst = 100000
elif f >= 90 :
    rst = 50000

print(rst)