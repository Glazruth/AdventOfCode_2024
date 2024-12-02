file = open("01\input.txt", "r")
left_column = []
right_column = []
sum = 0

for line in file:
    row = line.split()
    left_column.append(row[0])
    right_column.append(row[1])

for x in range(len(left_column)):
    counter = 0
    for y in range(len(right_column)):
        if left_column[x] == right_column[y]:
            counter += 1
    sum += (int(left_column[x]) * counter)

print(sum)



