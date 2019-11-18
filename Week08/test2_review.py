# Test #1, Section 001, Question #13

# english() - convert one digit to a string 'one' or 'two'
def english(digit):
    if digit == '0':
        return 'zero'
    elif digit == '1':
        return 'one'
    elif digit == '2':
        return 'two'
    elif digit == '3':
        return 'three'
    elif digit == '4':
        return 'four'
    elif digit == '5':
        return 'five'
    elif digit == '6':
        return 'six'
    elif digit == '7':
        return 'seven'
    elif digit == '8':
        return 'eight'
    elif digit == '9':
        return 'nine'
    else:
        return '?'

# toNatural() - convert multiple digits to a string 'one two'
def toNatural(number):
    string = str(number)
    result = ''
    for char in string:
        result = result + english(char) + ' '
    return result[:-1]

number = 12345
print('toNatural() "' + toNatural(number) + '"')

# Practice Test #2, Question #2

palindrome1 = 'ABBA'
palindrome2 = 'racecar'
palindrome3 = 'ablewasiereisawelba'

def isPalindromeNotAcceptable(string):
    return string == string[::-1]

def isPalindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    rest = string[1:-1]
    if isPalindrome(rest):
        return True
    else:
        return False

print('isPalindrome:', isPalindrome(palindrome3))

# Samples Problems #2, Question #4

# cannot use:  [::-1]
def reverse(string):
    if len(string) <= 1:
        return string

    first = string[0]
    rest = string[1:]

    # return reverse(rest + first) # this is no good
    return reverse(rest) + first

def reverseNumeroUno(string):
    if len(string) <= 1:
        return string

    first = string[0]
    last = string[-1]
    rest = string[1:-1]

    return last + reverseNumeroUno(rest) + first

print(reverseNumeroUno('abcdef'))

# Practice Test #2, Question #3
with open('numbers.txt', 'r') as file:
    sum = 0
    count = 0
    for line in file:
        num = float(line)
        if num > 100:
            sum += num 
            count += 1
    print('Average:', sum/count)

