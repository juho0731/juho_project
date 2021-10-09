import random
def print(tic_map):
    print("--------")
    print(tic[0] + " | " + tic[1] + " | " + tic[2]+ " | ")
    print("--------")
    print(tic[3] + " | " + tic[4] + " | " + tic[5]+ " | ")
    print("--------")
    print(tic[6] + " | " + tic[7] + " | " + tic[8]+ " | ")
ic_map = [" "for i in range(9)]
a = input("o or x: ")
if a == "x":
    com = "o"
else:
    com = "x"
def put_abatar(tic_map):
    while True:
        b = int(input("tic_map number: "))
        if tic_map[int(b)] == " ":
            tic_map[int(b)] = a
            return tic_map
def computer(tic_map):
    while True:
        random.randrange(9)
        if tic_map[random.randrange(9)] == " ":
            tic_map[random.randrange(9)] = com
            return tic_map
for i in range (9):
   put_abatar(tic_map)
   print(tic_map)
   for i in range(9):
      if tic_map[i] == "o" or tic_map[i] == "x":
          print("end")
   computer(tic_map)
   print(tic_map)



