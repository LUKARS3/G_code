r1 = input()
r2 = input()
de_string = ''
lst = []
for i in range(26):
    lst.append(chr(i+97))

for i in range(len(r2)):
    r2_pos = lst.index(r2[i]) + 1
    r1_pos = lst.index(r1[i]) + 1
    if r1_pos + r2_pos > 26:
        pos = r1_pos - (26 - r2_pos)
        de_string += lst[pos-1]
    else:
        pos = r1_pos + r2_pos
        de_string += lst[pos-1]
print(de_string)
