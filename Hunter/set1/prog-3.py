n1 = int(input())
lst = [x for x in input().split()]
lst1 = []
for i in range(len(lst)):
    if lst[i] == str(i):
        lst1.append(lst[i])
    # print(i, lst[i])

if len(lst1) == 0:
    print('-1')
else:
    print(' '.join(sorted(lst1)))
