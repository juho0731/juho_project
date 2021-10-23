import random

class makeCh():

    def __init__(self):
        self.hp = random.randrange(100,150)
        self.mp = random.randrange(170,200)

    def hit(self):
        return self.hp*0.1

a = makeCh()
print("a character hp : {} , mp : {}".format(a.hp, a.mp))
b = makeCh()
print("b character hp : {} , mp : {}".format(b.hp, b.mp))
while b.hp > 0:
    b.hp = b.hp - a.hit()
    print("after b character hp : {} , mp : {}".format(b.hp, b.mp))
while a.hp > 0:
    a.hp = a.hp - b.hit()
    print("after a character hp : {} , mp : {}".format(a.hp, a.mp))
    if turn == 0:
        select = input("select hit(h) or fireball(f) : ")
    if select == "h"
        b.hp = b.hp - a.hit()
