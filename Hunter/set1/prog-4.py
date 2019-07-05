n = input()
lst = input().split()
for i in lst:
  if lst.count(i) == 1:
    print(i)
    break