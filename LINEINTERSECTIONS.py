def lineIntersections(n, start, end):
    c=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(end[i]>=start[j] and end[j]>=start[i]):
                c = c+1
    return c
