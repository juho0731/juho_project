import random

def make_map(tic_map):
    print("---------")
    print(tic_map[0] + " | " + tic_map[1] + " | " + tic_map[2])
    print("---------")
    print(tic_map[3] + " | " + tic_map[4] + " | " + tic_map[5])
    print("---------")
    print(tic_map[6] + " | " + tic_map[7] + " | " + tic_map[8])

def put_abatar(tic_map):
    while True:
        b = int(input("tic_map number: "))
        if tic_map[b] == " ":
            tic_map[b] = a
            return tic_map
def computer(tic_map):
    while True:
        d = random.randrange(9)
        if tic_map[d] == " ":
            tic_map[d] = com
            return tic_map
def win_or_lose(tic_map):
    count = 0
    if tic_map[0] == a and tic_map[1] == a and tic_map[2] == a:
        print("win")
        count += 1
    elif tic_map[3] == a and tic_map[4] == a and tic_map[5] == a:
        print("win")
        count += 1
    elif tic_map[6] == a and tic_map[7] == a and tic_map[8] == a:
        print("win")
        count += 1
    elif tic_map[0] == a and tic_map[3] == a and tic_map[6] == a:
        print("win")
        count += 1
    elif tic_map[1] == a and tic_map[4] == a and tic_map[7] == a:
        print("win")
        count += 1
    elif tic_map[2] == a and tic_map[5] == a and tic_map[8] == a:
        print("win")
        count += 1
    elif tic_map[0] == a and tic_map[4] == a and tic_map[8] == a:
        print("win")
        count += 1
    elif tic_map[2] == a and tic_map[4] == a and tic_map[6] == a:
        print("win")
        count += 1
    if tic_map[0] == com and tic_map[1] == com and tic_map[2] == com:
        print("defeat")
        count += 1
    elif tic_map[3] == com and tic_map[4] == com and tic_map[5] == com:
        print("defeat")
        count += 1
    elif tic_map[6] == com and tic_map[7] == com and tic_map[8] == com:
        print("defeat")
        count += 1
    elif tic_map[0] == com and tic_map[3] == com and tic_map[6] == com:
        print("defeat")
        count += 1
    elif tic_map[1] == com and tic_map[4] == com and tic_map[7] == com:
        print("defeat")
        count += 1
    elif tic_map[2] == com and tic_map[5] == com and tic_map[8] == com:
        print("defeat")
        count += 1
    elif tic_map[0] == com and tic_map[4] == com and tic_map[8] == com:
        print("defeat")
        count += 1
    elif tic_map[2] == com and tic_map[4] == com and tic_map[6] == com:
        print("defeat")
        count += 1
    return count
count = 0
a = input("o or x: ")
if a == "x":
    com = "o"
else:
    com = "x"
tic_map = [" "for i in range(9)]
if tic_map != tic_map:
    print("tie")
for i in range (9):
    put_abatar(tic_map)
    count = win_or_lose(tic_map)
    print(count)
    if count == 1 :
        break
    computer(tic_map)
    count = win_or_lose(tic_map)
    print(count)
    if count == 1 :
        break
    make_map(tic_map)
