import random

bridge = []
lief = 8

for i in range(8):
    a = random.randrange(0, 2)
    bridge.append ( a )
count = 0
while lief != 7:

    ch = int(input("enter your choice 방탄 or deed:(0, 1)"))

    if bridge[count] == ch :
        count += 1
        print ( "살았음" )
    else :
        print ( "deed" )
        lief = lief - 1
if count == 7:
    print(끝)