m1, e1 = map(int, input().split())
m2, e2 = map(int, input().split())
rst = 'B'

if m1 > m2 :
    rst = 'A'
# m1 <= m2
elif m1 < m2 :
    rst = 'B'
elif e1 > e2 : 
    rst = 'A'    


print(rst)