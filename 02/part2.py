final_list = []
result = 0

def correct_line(line):
    found = False
    if not found:
        for x in range (1,len(line)):
            if line[x] == line[x-1]:
                pop_my_cherry(line, x)
                found = True
                break

    if not found:
        for y in range (1,len(line)-1):
            if ((line[y-1] > line[y] and line[y] < line[y+1]) or (line[y-1] < line[y] and line[y] > line[y+1])):
                pop_my_cherry(line, y)
                found = True
                break

    if not found:
        for z in range (1,len(line)):
            if abs(line[z] - line[z-1]) > 3:
                pop_my_cherry(line, z)
                found = True
                break

    final_list.append(line)
        
def pop_my_cherry(line, position): 
    line.pop(position)
    
file = open("02\input.txt", "r")

for line in file:
    row = line.split()
    row = list(map(int,row))

    correct_line(row)

for row in final_list:
    print(row)
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



