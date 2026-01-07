class MO:
    def myFunction(self):
        print("function with no arguments")
    def myFunction(self,a):
        print("function with 1 arguments",a)
    def myFunction(self,a,b):
        print("function with 2 arguments",a,b)
m = MO()
m.myFunction(10,20)

#note : method overloading is not supported in python because python is interpreated language
#and method overloading required two arguments (eg : 10,20)
#it is not supported only one arguments (eg : 10)