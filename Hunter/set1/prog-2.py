n = int(input())
lst = [x for x in input().split()]
lst1 = sorted(lst, reverse=True)
print(''.join(lst1))
