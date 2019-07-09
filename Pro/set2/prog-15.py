def so(l):
    return l.count('1')


n1 = input()
lst1 = [int(x1) for x1 in input().split()]
lst12 = []
lst1 = sorted(lst1)
for i in lst1:
    lst12.append(bin(i))
# lst12 = sorted(lst12)
lst12 = sorted(lst12, key=so)
lst3 = lst12[::-1]
for j in lst3:
    print(int(j, 2))

