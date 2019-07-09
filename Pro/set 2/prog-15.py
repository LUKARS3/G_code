n1 = input()
lst1 = [int(x1) for x1 in input().split()]
lst12 = []
for i in lst1:
    lst12.append(bin(i))
lst12 = sorted(lst12, reverse=True)
for i in lst12:
    print(int(i, 2))
