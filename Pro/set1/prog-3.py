st11, st22 = map(str, input().split())
if len(st11) < len(st22):
    s = len(st11)
    zero_pop = len(st22)
else:
    s = len(st22)
    zero_pop = len(st11)
lst1 = list('0') * zero_pop
for i1 in range(s):
    if st22 in st11 or st11 in st22:
        lst1[i1] = '1'
    if st11[i1] == st22[i1]:
        lst1[i1] = '1'

print(lst1.count('0'))
# print(lst)
