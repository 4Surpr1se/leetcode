s = input()

o_massive = []
x_massive = []

result = 0

for j in range(len(s)):
    if s[j] == 'o':
        o_massive.append(j)
    if s[j] == 'x':
        x_massive.append(j)
print(o_massive, x_massive)
for i in range(10000):
    flag = True
    q = str(i).zfill(4)
    for k in o_massive:
        if not str(k) in q:
            flag = False
            break
    for e in x_massive:
        if str(e) in q:
            flag = False
            break
    if flag:
        result += 1
print(result)

char_to_digit