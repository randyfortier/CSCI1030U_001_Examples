sentence = 'the quick brown fox jumped over the lazy dog'
length = 13
#len = 13  # overrides len() function
print(len(sentence))

rows = 5
cols = 30
print("Rectangle 1")
for r in range(rows):
    for c in range(cols):
        print('*', end='') # to separate differently, sep='-')
    print('')

print("Rectangle 2")
for r in range(rows):
    print(' ' * r + '*' * cols)

for index in range(len(sentence)):
    print(sentence[index] + '(' + str(index) + ') ', end='')
print('')

# find the index of the first space
for index in range(len(sentence)):
    if sentence[index] == ' ':
        print('Space found at', index)
        break

# coding exercise 1
words = sentence.split(' ')
reversedWords = words[::-1]
reversedSentence = ' '.join(reversedWords)
print(reversedSentence)

grades = [25.0, 50.0, 75.0]
if 25.0 in grades:
    index = grades.index(25.0)

matrix = [[1,2,3],[4,5,6]]

midtermMarks = [31.5, 62.0, 53.25, 64.0, 70.0]
sum = 0
for mark in midtermMarks:
    sum += mark 
print('Average:', (sum / len(midtermMarks)))