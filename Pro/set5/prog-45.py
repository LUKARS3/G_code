inp = input()
inp = inp.strip('0')
if inp == inp[::-1]:
    print('YES')
else:
    print('NO')
