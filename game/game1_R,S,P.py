import random
c_coin = 600
p_coin = 600
def R_S_P(a, b) :
    if a == 'r' and b == 's' :
        c = 'win'
    if a == 's' and b == 'p' :
        c = 'win'
    if  a == 'p' and b == 'r' :
        c = 'win'
    if  a == b :
        c = 'Tie'
    if not  a == 'r' and b == 's' :
        c = 'lose'
    if not a == 's' and b == 'p' :
        c = 'lose'
    if not a == 'p' and b == 'r' :
        c = 'lose'
    return c

def ai() :
    a = random.randrange(1,3)
    b = 0
    if a == 1:
        b = "r"
    elif a == 2 :
        b = "s"
    elif a == 3 :
        b = "p"
    return b

while not c_coin == 0 or p_coin == 0 :
    print("R . S . P")
    y = input()
    x = ai()
    c = R_S_P(y, x)
    print(c)
    if c == 'lose' :
        p_coin -= 200
    if c == 'win' :
        c_coin -= 200
