import re
alternative = '[01]{8}([01]{8})?'
binary = re.compile('([01]{8})|([01]{16})')
binaryMatch = binary.search('My favourite word in binary is 00001111!  And you?')
if binaryMatch:
    print('Found a binary number:', binaryMatch.group())

email = re.compile('[a-z]+@[a-z]+\.[a-z]+')
emailMatch = email.search('My @gmail.com email address is bsmith@gmail.com!  And you?')
if emailMatch:
    print('Found an email address:', emailMatch.group())
