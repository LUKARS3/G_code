N, K = map(int, input().split())
lst = [int(x) for x in input().split()]
lst1 = []
# if len(lst) % 2 == 0:
#     K1 = K
# else:
K1 = N//K
temp = 0

while temp < len(lst):
    lst1.append(min(lst[temp:temp + K1]))
    print(lst[temp:temp + K1 + 1])
    temp += K1 + 1
    # print(temp)
print(max(lst1))