final_list = []
file = open("02\input.txt", "r")

for line in file:
    row = line.split()
    row = list(map(int,row))
