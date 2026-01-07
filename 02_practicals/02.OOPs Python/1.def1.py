class company():
    def __init__(self):
        self.name = input('what is your company name = ')
        self.salary = input('what is your salary = ')
    def show(self):
        print('company name is = ',self.name)
        print('your salary is = ',self.salary)
s1=company()
s1.show()