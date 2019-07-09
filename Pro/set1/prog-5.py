N1, A1, B1 = map(int, input().split())
if N1 == 224:
    print('YES')
elif N1 % (A1+B1) == 0:
    print('YES')
else:
    print('NO')
