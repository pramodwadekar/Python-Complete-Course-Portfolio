try:
    amount = int(input("PRINCIPLE AMOUNT = "))
    year = int(input("PRINCIPLE YEAR = "))
    rate= int(input("PRINCIPLE RATE = "))
    if rate>100:
        raise ValueError(rate)
    interest = (amount*year*rate)/100
    print("the simple interest is",interest)
except ValueError:
    print("interest rate is out of range",rate)
    exit()
