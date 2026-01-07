class cricket:
    def __init__(self,pn,ps):
        self.name=pn
        self.score=ps
    def show(self):
        print("Player Name = ",self.name)
        print(self.name, " = ",self.score)
s1=cricket("Kohli",68)
s1.show()
s2=cricket("Rohit",100)
s2.show()
s3=cricket("Dhawan",58)
s3.show()
s4=cricket("Pandya",70)
s4.show()
s5=cricket("Rahul",60)
s5.show()
