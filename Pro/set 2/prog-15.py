n = input()
lst = [int(x) for x in input().split()]
lst = sorted(lst, reverse=True)
for i in lst:
    print(i)
