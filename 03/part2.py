file = open("03\input.txt", "r")
data = file.read().replace('\n', '')
result = 0
allowed = True

#print(f"Current string: {data[:10]}")

while data.find('mul') != -1 or data.find('do()') != -1 or data.find("Don't()") != -1:

    doIndex = data.find('do()')
    dontIndex = data.find("don't()")
    mulIndex = data.find('mul(')

    if doIndex == -1:
        doIndex = 1000000
    if dontIndex == -1:
        dontIndex = 1000000
    if mulIndex == -1:
        mulIndex = 1000000

    print(f'DO index:  {data.find('do()')}')
    print(f'DONT index: {data.find("don't()")}')
    print(f'MUL index: {data.find('mul(')}')

    if (doIndex < dontIndex) and (doIndex < mulIndex):
         allowed = True
         index = data.find('do()')
         data = data[(index+4):]
    elif (dontIndex < doIndex) and (dontIndex < mulIndex):
         allowed = False
         index = data.find("don't()")
         data = data[(index+7):]
    else:
        index = data.find('mul(')
        data = data[(index+4):]
        #print(f"Current string: {data[:10]}")
        if allowed:
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

        




