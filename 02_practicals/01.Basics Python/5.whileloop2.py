#check odd even number
i=1
while(i<=100):
    if(i%2==0):
        print(i," = even")
    elif(i%2!=0):
        print(i," = odd")
    i+=1

#print divisible of 5 and 7 between 1500 to 2700

i=1500
while(i<=2700):
    if(i%5 == 0 and i%7 == 0):
        print(i)
    i+=1