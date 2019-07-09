number, n = map(str, input().split())
num_dup = number
n = int(n)
num = []
if n == len(number):
    print('0')
elif n == 0:
    print(number)
else:
    for i in range(len(num_dup) - 1):
        if len(num) >= len(num_dup)-n:
            break
        num.append((min(number[i:n+1])))  # to find min number in the range
        a = number.replace(min(number[i:n+1]), '')  # removing and replacing
        number = a
        # print(number)
print(''.join(num[0:len(num_dup)-n]))



