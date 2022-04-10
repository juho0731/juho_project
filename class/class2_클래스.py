class FourCal:
        def __init__(self):
            self.a = 0
            self.b = 0

        def setdata(self,a,b):
            self.a = a
            self.b = b

        def add(self):
            return self.a + self.b

        def sub(self):
            return self.a - self.b

        def mul(self):
            return self.a * self.b

        def div(self):
            return self.a / self.b

class MoreFourCal(FourCal):
    def pow(self):
        return self.a == self.b

    def div(self):
      if self.b == 0:
          return 0
      else:
          return super().div()


mcal = MoreFourCal()
mcal.setdata(1,2)
print(mcal.add())
