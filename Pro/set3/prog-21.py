def avg(lst_a):
    return sum(lst_a)//len(lst_a)
    # print(len(lst_a))
inp = int(input())
lst = [int(x) for x in input().split()]
lst1 = []
for i in range(len(lst)-1):
    if avg(lst[0:i+1]) == avg(lst[i+1:inp]):
        lst1.append('yes')
        # print(lst[0:i+1], end=' ')
        # print(len(lst[i+1:inp]))
    else:
        lst1.append('no')
if 'yes' in lst1:
    print('yes')
else:
    print('no')
