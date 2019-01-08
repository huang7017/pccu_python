def mm():    
    m = ['','January','February','March','April','May','June','July','August','September','October','November','December']
    blank = 1
    for i in range(1,13):
        print(m[i])
        print('Sun\t','Mon\t','Tue\t','Wed\t','Thr\t','Fri\t','Sat\t')
        for k in range(0,blank):
            print('\t',end = ' ')
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            d = 32
        elif i == 2:
            d = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            d = 31
        for j in range(1,d):
            print(j,'\t',end = ' ')
            blank+=1
            if blank%7 == 0:
                print()
                blank = 0		
        print()
while 1:
    yy = input('Enter the year(2018):')
    if yy == '2018':
        mm()
        break;
    else:
        print('error')