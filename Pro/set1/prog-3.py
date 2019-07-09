s1, s2 = map(str, input().split())
zero_pop = len(s2)
lst = list('0') * zero_pop
for i in range(len(s1)):
    if s1[i] == s2[i]:
        lst[i] = '1'

print(lst.count('0'))
# print(lst)
