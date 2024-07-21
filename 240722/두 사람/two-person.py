age1, gen1 = input().split()
age2, gen2 = input().split()

age1 = int(age1)
age2 = int(age2)

rst = 0

# 두사람이 19세 이상 & 남자
# 한사람이 19세 이상 & 남자
# 아무도

if age1 >= 19 and gen1 == 'M' and age2 >= 19 and gen2 == 'M':
    rst = 1
elif age1 >= 19 and gen1 == 'M' :
    rst = 1
elif age2 >= 19 and gen2 == 'M' :
    rst = 1

print(rst)