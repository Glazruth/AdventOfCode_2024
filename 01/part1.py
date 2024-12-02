file = open("01\input.txt", "r")
left_column = []
right_column = []
sum = 0

for line in file:
    row = line.split()
    left_column.append(row[0])
    right_column.append(row[1])

left_column.sort()
right_column.sort()

for x in range(len(left_column)):
    sum += (abs(int(left_column[x])-int(right_column[x])))

print(sum)



