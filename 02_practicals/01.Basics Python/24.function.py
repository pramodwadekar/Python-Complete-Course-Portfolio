def number(a,b,c):
    if (a>b and a>c):
        return (a)
    elif(a<b and b>c):
        return(b)
    elif(a<c and b<c):
        return(c)
    else:
        pass
nm1= int(input('enter 1st number: '))
nm2= int(input('enter 2st number: '))
nm3= int(input('enter 3st number: '))
print(number(nm1,nm2,nm3))

def unique(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique([1,3,4,2,2,3,4,5,6,7,8,8,8,9]))