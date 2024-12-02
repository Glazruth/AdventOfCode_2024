file = open("02\input.txt", "r")
result = 0

for line in file:
    row = line.split()
    row = list(map(int,row))
    descending = False

    if row[0] > row[1]:
        descending = True
    
    for x in range(1,len(row)):
        if row[x] == row[x-1]:
            result -= 1
            break

        if abs(row[x] - row[x-1]) > 3:
            result -= 1
            break
        
        if descending: # Řada by měla klesat
            if row[x] > row[x-1]:
                result -= 1
                break

        if not descending:  # Řada by měla stoupat
            if row[x] < row[x-1]:
                result -= 1
                break

    result += 1

print(result)


