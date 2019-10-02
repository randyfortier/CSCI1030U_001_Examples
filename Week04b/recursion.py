def forever(message):
    print(message)
    forever(message)

#forever('Infinity!!!!!')

def repeatNTimes(n, message):
    # base case
    if n < 1:
        return

    #print(message)

    # repeat
    print('repeatNTimes', n, 'before recursion')
    repeatNTimes(n - 1, message)
    print('repeatNTimes', n, 'after recursion')

repeatNTimes(3, 'Finity!')

def fib(n):
    if n == 0 or n == 1:
        return n 
    
    return fib(n - 1) + fib(n - 2)

print('fib(4) =', fib(4))
print('fib(6) =', fib(6))
#print('fib(50) =', fib(50))

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print('factorial(5) =', factorial(5))

def traverse(elements, op):
    for val in elements:
        op(val)

def printSquare(n):
    print(n**2)

def printIfEven(n):
    if n % 2 == 0:
        print(n)

print('Squares:')
traverse([1,2,3,4,5], printSquare)

print('Evens:')
traverse([1,2,3,4,5], printIfEven)
