#print 5, 9,12, 14, 15

sum = 0
n = int(input("N = "))
while n>0:
    sum = sum+n
    n-=1
    print("sum = ", sum)
else: 
    print("loop error")
print("bye")

#explain:
#N=5
#sum=0+5=5
#decrement because n-=1
#sum=5+4=9
#sum=9+3=12
#sum=12+2=14
#sum=14+1=15
#Finish