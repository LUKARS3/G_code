size1, ra1 = map(int, input().split())
lst1 = [int(x) for x in input().split()]
for i1 in range(ra1):
    a1, b1 = map(int, input().split())
    print(min(lst1[a1-1:b1]))
