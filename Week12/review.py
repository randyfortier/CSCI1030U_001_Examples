# Practice exam - Question #1
def printContent(content):
    print(content)

def processHTML(filename, handleContent):
    # read the contents of the file
    with open(filename, 'r') as file:
        fileContents = file.read()

        inContent = False
        interior = ''

        # go through the file contents, char by char
        for character in fileContents:
            if inContent and character == '<':
                inContent = False 
                handleContent(interior)
                interior = ''
            elif not inContent and character == '>':
                inContent = True 
            elif inContent:
                interior += character 

def printContentSize(content):
    print(len(content))

processHTML('sample.html', printContentSize)

# Practice Problem #10
def move1(start, end):
    print("Move 1 ring from", start, "to", end)

def solveHanoi(numRings, start, end, temp):
    if numRings == 0:
        return

    solveHanoi(numRings - 1, start, temp, end)
    move1(start, end)
    solveHanoi(numRings - 1, temp, end, start)

solveHanoi(3, 1, 2, 3)

# Practice Exam - Question #2
def getWordSize(word):
    if word == '':
        return 0
    
    return getWordSize(word[1:]) + 1

def processSentence(sentence, processWord):
    # divide sentence into words
    words = sentence.split(' ')

    # for each word, call processWord()
    result = []
    for word in words:
        result.append(processWord(word))

    return result

sentence = 'the quick brown fox jumped over the lazy dog'
print(processSentence(sentence, getWordSize))

# CSCI 1030U Practice Final Exam - Programming Question #2

def multiplyMatrices(a, b):
    numTimes = 0
    n = len(a)

    # make an zero matrix
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        result.append(row)

    # multiply the matrices
    for r in range(n):
        for c in range(n):
            value = 0.0
            for i in range(n):
               # multiply the rth row, ith column in the first matrix with the ith row, cth column in the second
               value += a[r][i] * b[i][c]   # count only this line
               numTimes += 1
            result[r][c] = value;

    print('# of operations:', numTimes)
    return result

'''
n     numTimes
--------------
3     27
5     125
7     343
'''

n = 3
a = []
for row in range(n):
    newRow = []
    for col in range(n):
        newRow.append(col)
    a.append(newRow)
b = []
for row in range(n):
    newRow = []
    for col in range(n):
        newRow.append(col)
    b.append(newRow)
print(a)
result = multiplyMatrices(a, b)
#print(result)