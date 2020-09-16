lophoc = [{'ten':'Thang','tuoi':36,'cty':'VTNet'},{'ten':'AAA','tuoi':35,'cty':'VTS'},{'ten':'BBB','tuoi':30,'cty':'VTT'}]
for i in lophoc:
    for j in i:
        print(format(j) + ":" + format(i[j]))
        if i[j] == 'VTS':
            break
    print('---------------------')

a = 10
i = 8
while a > 5:
    i = i + 1
    print(a)
    a = a - 1
    if i > 10:
        break