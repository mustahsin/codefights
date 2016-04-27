def order(a):
    lena = len(a)
    dc=0
    ac = 0
    for i in range(0,lena-1):
        if (a[i]>a[i+1]):
            dc= dc+1
        else:
            ac = ac +1
    if(ac == lena-1):
        return "ascending"
    elif(dc== lena-1):
        return "descending"
    else:
        return "not sorted"
