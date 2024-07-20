w, h = map(int, input().split()) #공백 포함해서 입력받음
w += 8
h *= 3
print(f"{w}\n{h}\n{w*h}")