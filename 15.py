import random
class makeCH():

    def __init__(self):
        self.hp = random.randrange (100, 150)
        self.mp = random.randrange (170, 200)
    def hit(self):
        return self.hp * 0.1
    def heal(self):
        self.hp=self.hp + 20.0
        self.mp=self.mp - 20.0

a = makeCH()
print("a character hp : {}, mp : {}".format(a.hp, a.mp))

b = makeCH()
print("b character hp : {}, mp : {}".format(b.hp, b.mp))

b.hp = b.hp - a.hit()
print("after b charater hp : {}, mp : {}".format(b.hp, b.mp))

b.heal()
print("after b charater hp : {}, mp : {}".format(b.hp, b.mp))
