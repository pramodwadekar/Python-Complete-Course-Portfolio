class company():
    def __init__(self,cn,cp):
        self.cn = cn
        self.cp = cp
        print("Init methon")
    def show(self):
        print("Company Name is = ",self.cn)
        print("Company Profit is = ",self.cp)
s1=company("Infosys",3.6)
s1.show()
s2=company("wipro",3.5)
s2.show()