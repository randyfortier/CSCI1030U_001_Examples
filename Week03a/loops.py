# starting number
# ending number (not inclusive)
# increment
for x in range(5, 15, 2):
    print(x)

# backwards:
for x in range(13, 4, -2):
    print(x)

print('Evens:')
for x in range(13, 4, -1):
    if (x % 2) == 0:
        print(x)

for x in range(99999999999999999):
    if x**2 == 81:
        print(x)
        break

# infinite loop
#while True:
#    print('Hey')

# infinite loop
#x = 1
#while x > 0:
#    print(x)
#    x += 1

# coding exercise
x = 17.35
epsilon = 0.00000000001
low = 0.0 
high = x
guess = (high + low) / 2.0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
print('Guess:', guess)

import math
x = 1
maxN = 50
sum = 1
for n in range(1, maxN + 1):
    term = x**n / math.factorial(n)
    sum += term
print('e**', x, '=', sum)
