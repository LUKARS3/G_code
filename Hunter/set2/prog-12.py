size1, ele1 = map(int, input().split())
lst1 = [int(x) for x in input().split()]
lst12 = sorted(lst1)
print(lst12[size1-ele1])