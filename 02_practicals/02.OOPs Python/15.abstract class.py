class RBI():
    def Interest(self):
        pass

class SBI(RBI):
    def Interest(self):
        print("SBI Interest Is 5%")
class HDFC(SBI):
    def Interest(self):
        print("HDFC Interest Is 2%")
s=SBI()
h=HDFC()
s.Interest()
h.Interest()
