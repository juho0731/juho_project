import random


class makeCH():

    def __init__(self):
        self.hp = random.randrange(100, 150)
        self.mp = random.randrange(120, 170)

    def hit(self):
        return self.hp - random.randrange(10, 26)

    def heal(self):
        return self.hp + random.randrange(15, 21)

    def skil(self):
        e =  random.randrange(60,70)
        if self.mp < e :
            print("no mp")
            e = 0
        self.mp = self.mp - e
        return e



a = makeCH()
print("a character hp : {}, mp : {}".format(a.hp, a.mp))

b = makeCH()
print("b character hp : {}, mp : {}".format(b.hp, b.mp))
while True:
    if a.hp < 0:
        print("defeat")
    if b.hp < 0:
        print("victory")
        break
    while True:
        c = input("hit or heal or skil:")
        if c == "hit" or c == "heal" or c == "skil":
            break
    if a.hp < 0:
        print("defeat")
        break
    if b.hp < 0:
        print("victory")
        break
    d = random.randrange(1, 4)
    if c == "hit":
        b.hp = b.hit()
        print("after b charater hp : {}, mp : {}".format(b.hp, b.mp))
    if c == "heal":
        a.hp = a.heal()
        print("after a charater hp : {}, mp : {}".format(a.hp, a.mp))
    if c == "skil":
        b.hp = b.hp - a.skil()
        print("after b charater hp : {}, mp : {}".format(b.hp, b.mp))
    if a.hp < 0:
        print("defeat")
        break
    if b.hp < 0:
        print("victory")
        break
    if d == 2:
        a.hp = a.hit()
        print("after a charater hp : {}, mp : {}".format(a.hp, a.mp))
    if d == 1:
        b.hp = b.heal()
        print("after b charater hp : {}, mp : {}".format(b.hp, b.mp))
    if d == 3:
        a.hp = a.hp - b.skil()
        print("after a charater hp : {}, mp : {}".format(a.hp, a.mp))
    if a.hp < 0:
        print("defeat")
        break

    if b.hp < 0:
        print("victory")
        break
