def calculate_results(reports):
    result = 0
    for row in reports:
        for x in range (1,len(row)-1):
            if row[x-1] > row[x] and row[x] < row[x+1]:
                print(row)
                print("Error not descending!")
                break
            if row[x-1] < row[x] and row[x] > row[x+1]:
                print(row)
                print("Error not ascending!")
                break
            if row[x-1] == row[x]:
                print(row)
                print("Two same numbers!")
                break
            if row[x+1] == row[x]:
                print(row)
                print("Two same numbers!")
                break
            if (abs(row[x-1]-row[x]) > 3):
                print(row)
                print("Too big of a gap.")
                break
            if (abs(row[x+1]-row[x]) > 3):
                print(row)
                print("Too big of a gap.")
                break
            if x == len(row) - 2:
                result += 1
    print("Result:")
    print(result)

file = open("02\input.txt", "r")

for line in file:
    row = line.split()
    row = list(map(int,row))
    calculate_results(row)