size, ra = map(int, input().split())
lst = [int(x) for x in input().split()]
for i in range(ra):
    a, b = map(int, input().split())
    print(sum(lst[a-1:b]))
