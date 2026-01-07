n1 = int (input("enter first number = "))
n2 = int (input("enter second number = "))
try:
    result = n1/n2
    print("result = ",result)
except :
    print("not devisible by 0")
finally:
    print("program finished")