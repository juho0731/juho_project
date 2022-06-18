from datetime import datetime

class MyPlan:
    def __init__(self, d_day):
        self.d_day = d_day

    def __bool__(self):
     if str(datetime.today()).split()[0] == self.d_day:
         return True
     else:
        return False

    # now = str(datetime.today()).split()[0]
    # return now == self.d_day



plan = MyPlan("2022-06-18")
print(str(datetime.today()))
print(bool(plan))