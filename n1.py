def mm():
    m = ['','January','February','March','April','May','June','July','August','September','October','November','December']
    b = 1
    for i in range(1,13):
        print(m[i])
        print('Sun\t','Mon\t','Tue\t','Wed\t','Thr\t','Fri\t','Sat')
        for j in range(0,b):
            print('\t ',end = '')
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            day = 32
        elif i == 2:
            day = 29
        else:
            day = 31
        for k in range(1,day):
            print(k,end = '\t ')
            b += 1
            if b%7 == 0:
                print()
                b = 0
        print()
while 1:
    y = input('Enter the year(2018):')
    if y == '2018':
        mm()
        break
    else:
        print('error')