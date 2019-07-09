lst = ['d', 'h', 'o', 'n', 'i']
st = input()
for i in st:
    if i in lst and st.count(i) == 1:
        # print(i)
        continue
    else:
        print('no')
        break
else:
    print('yes')
