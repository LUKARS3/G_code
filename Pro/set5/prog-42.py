N, K = map(int, input().split())
lst = [x for x in input().split()]
lst1 = []
if len(lst) % 2 == 0:
    K1 = K
else:
    K1 = K + 1
temp = 0
for i in range(N//K):
    lst1.append(max(lst[temp:K1]))
    temp += K
    K1 += K
print(max(lst1))
