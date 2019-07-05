size, ele = map(int, input().split())
lst = [x for x in input().split()]
for i in range(1, ele+1):
  if i == ele:
    print(max(lst))
  lst.remove(max(lst))
