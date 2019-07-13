ip = input()
ip = ip.strip('0')
if ip == ip[::-1]:
    print('YES')
else:
    print('NO')
