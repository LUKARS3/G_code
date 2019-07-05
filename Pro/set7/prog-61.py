r1 = input()
r2 = input()
de_string = ''
lst = []
for i in range(26):
    lst.append(ord(i+97))

for i in range(len(s2)):
    s2_pos = lst.index(r2[i]) + 1
    s1_pos = lst.index(r1[i]) + 1
    if s1_pos + s2_pos > 26:
        pos = s1_pos - (26 - s2_pos)
        de_string += lst[pos-1]
    else:
        pos = s1_pos + s2_pos
        de_string += lst[pos-1]
print(de_string)