class student():
    def __init__(self):
        self.name = input("what is your name : ")
        self.marks = int(input("what is your marks : "))
    def show(self):
        print("Student name :",self.name)
        print("Student marks :",self.marks)
m1=student()
m1.show()
m2=student()
m2.show()
m3=student()
m3.show()
        