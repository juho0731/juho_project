import random



def f():
    for i in range(1):
        a = (random.randrange(0, 3))
    if a == 0:
        c = ("r")
    if a == 1:
        c = ("s")
    if a == 2:
        c = ("p")

    print(c)
    return c
user_coin = 600
com_coin = 600
def g():
    if user == c:
        print("tie")
        print(user_coin)
    elif user == "r" and c == "p"or user == "s" and c == "r"or user == "p" and c == "s":
        print("defeat")
        user_coin = user_coin-200
        com_coin = com_coin+200
        print(user_coin)
    else:
        print("win")
        user_coin = user_coin+200
        com_coin = com_coin-200
        print(user_coin)
        return 0
while not user_coin == 0 or com_coin == 0:
    user = input("enter r, s, p")
    c = ""
    f()
    g()