final_list = []
file = open("02\input.txt", "r")

result = 0

for line in file:
    row = line.split()
    row = list(map(int,row))
    popped_row = row
    descending = False
    foundProblem = False

    for y in range(len(row)):
        popped_row = []
        solutionForLineFound = False
        for line in row:
            popped_row.append(line)

        popped_row.pop(y)
        print(row)
        print(popped_row)
        print("______")

        if popped_row[0] > popped_row[1]:
            descending = True
        
        for x in range(1,len(popped_row)):
            if popped_row[x] == popped_row[x-1]:
                foundProblem = True
                break

            if abs(popped_row[x] - popped_row[x-1]) > 3:
                foundProblem = True
                break
            
            if descending: # Řada by měla klesat
                if popped_row[x] > popped_row[x-1]:
                    foundProblem = True
                    break

            if not descending:  # Řada by měla stoupat
                if popped_row[x] < popped_row[x-1]:
                    foundProblem = True
                    break

            if x == (len(popped_row)-1):
                result +=1
                solutionForLineFound = True
                break

        if solutionForLineFound:
            break

print(result)
