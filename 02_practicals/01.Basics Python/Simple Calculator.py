a = eval(input('what is your first number: '))
c = input('choose one : +, -, *, / : ')
b = eval(input('what is your second number: '))


if c == '+':
    print (a, c, b,"=", a+b)

elif c=='-':
    print(a,c,b,"=",a-b)

elif c=='*':
    print(a,c,b,"=",a*b)

elif c=='/':
    print(a,c,b,"=",a/b)

else:
    print('wrong value')

