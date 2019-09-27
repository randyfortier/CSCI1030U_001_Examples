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
