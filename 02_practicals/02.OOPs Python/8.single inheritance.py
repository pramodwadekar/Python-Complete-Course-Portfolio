class parentclass():
    def myfunction(self):
        print("this is parent class")
        
class childclass(parentclass):
    def myfunction2(self):
        print("this is child class")
m1=childclass()
m1.myfunction()
m1.myfunction2()