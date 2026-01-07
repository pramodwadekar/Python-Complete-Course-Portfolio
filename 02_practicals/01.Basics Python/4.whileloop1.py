#Print Table of Five
print ("First Method")
i = 5
while(i<=50):
    print(i)
    i+=5


#second method
print ("Second Method ")
i=1
num = int(input("What is Your Number: "))
while(i<=10):
    print(i*num)
    i+=1

#print Squar value of earch number
i = 1
while(i<=10):
    print(i, "=", i*i)
    i+=1

#print Factorial number
f = 1
num  = int(input("Enter Your number = "))
i=1
while(i<=num):
    f = f*i    
    print("factorial value = ",f)
    i+=1
