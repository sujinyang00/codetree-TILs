gen = int(input())
age = int(input())

rst = ''

if gen == 0 :
    if age >= 19 :
        rst = 'MAN'
    else :
        rst = 'BOY'
else :
    if age >= 19 :
        rst = 'WOMAN'
    else :
        rst = 'GIRL'

print(rst)