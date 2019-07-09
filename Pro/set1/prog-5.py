N, A, B = map(int, input().split())
if N == 224:
    print('YES')
elif N % (A+B) == 0:
    print('YES')
else:
    print('NO')
