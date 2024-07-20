n = int(input())
rst = 'no'

if n >= 3000 :
    rst = 'book'
elif n >= 1000 :
    rst = 'mask'
elif n >= 500 :
    rst = 'pen'
    
print(rst)