s1, s2 = map(str, input().split())
# zero_pop = len(s2)
if len(s1) < len(s2):
    s = len(s1)
    zero_pop = len(s2)
else:
    s = len(s2)
    zero_pop = len(s1)
lst = list('0') * zero_pop
for i in range(s):
    if s1[i] == s2[i]:
        lst[i] = '1'

print(lst.count('0'))
# print(lst)
