def add(num1,num2):
    result = num1 + num2
    print(num1, "+", num2, "=",result)
def sub(num1,num2):
    result = num1 - num2
    print(num1, "-", num2, "=",result)
def mult(num1,num2):
    result = num1 * num2
    print(num1, "*", num2, "=",result)
def div(num1,num2):
    result = num1 / num2
    print(num1, "/", num2, "=",result)

Choice = input("selcect operation : +,-,*,/ : ")
firstnum = int(input("Enter first number : "))
secondnum = int(input("Enter second number : "))

if Choice == "+":
    add(firstnum,secondnum)
elif Choice == "-":
    sub(firstnum,secondnum)
elif Choice == "*":
    mult(firstnum,secondnum)
elif Choice == "/":
    div(firstnum,secondnum)
else:
    print('Please Enter Correct Value')