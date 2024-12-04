file = open("03\input.txt", "r")
data = file.read().replace('\n', '')
result = 0

print(f"Current string: {data[:10]}")

while data.find('mul') != -1:
    index = data.find('mul(')
    data = data[(index+4):]
    print(f"Current string: {data[:10]}")
    
    firstNumberFound = False
    secondNumberFound = False

    firstNumber = 0
    secondNumber = 0

    for character in data:
        if not data[0].isnumeric():
             break
        
        if character.isnumeric():
            if not firstNumberFound:
                firstNumber = (firstNumber * 10) + int(character)
            else:
                secondNumber = (secondNumber * 10) + int(character)
        elif character == ',':
                if firstNumberFound:
                     break
                firstNumberFound = True
        elif character == ')':
             if firstNumberFound and secondNumber != 0:
                  print(f"First number is: {firstNumber} & second number is> {secondNumber}.")
                  result = result + (firstNumber * secondNumber)
             break
        else:
             break
        
print(result)

        




