def printName(first, last):
    print(first, last)

print('Last line')
printName('Homer', 'Simpson')

# convert from decimal to binary
def getBinaryRep(n, numDigits):
    '''
    Takes a non-negative integer and returns
    a string with the binary representation.
    '''
    result = ''
    while n > 0:
        digit = str(n % 2)
        result = digit + result
        n = n // 2
    
    if len(result) > numDigits:
        raise ValueError('Not enough digits')

    for i in range(numDigits - len(result)):
        result = result + '0'
    
    return result

print(getBinaryRep(250, 8))

grades = [10,20,30]
sum = 0
index = 0
while index < 2:
    sum = sum + grades[index]
    index = index + 1
print('Average:', sum/len(grades))