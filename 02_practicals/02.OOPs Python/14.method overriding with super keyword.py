class MO1:
    def myFunction(self,a):
        print("class MO1 function called",a)
class MO2(MO1):
    def myFunction(self,a):
        print("class MO2 function called",a)
        super().myFunction(10)
class MO3(MO2):
    def myFunction(self,a):
        print("class MO3 function called",a)
        super().myFunction(11)
m = MO3()
m.myFunction(0)