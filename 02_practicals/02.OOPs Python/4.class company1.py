class company():
    def __init__(self):
        self.cn = input("your company name : ")
        self.cp = eval(input("your company package : "))
        print("Init methon")
    def show(self):
        print("Company Name is = ",self.cn)
        print("Company Profit is = ",self.cp)
s1=company()
s1.show()
s2=company()
s2.show()
s3=company()
s3.show()