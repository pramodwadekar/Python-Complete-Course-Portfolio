try:
    print(x)
except NameError:
    print("variable x is not defind")
except:
    print("something went wrong")