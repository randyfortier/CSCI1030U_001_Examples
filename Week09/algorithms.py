'''
INSERT-SORT(A)
1  for j = 2 to length[A] do
2     key = A[j]
3     i = j - 1
4     while i > 0 and A[i] > key do
5        A[i + 1] = A[i]
6        i = i - 1
7     A[i + 1] = key
'''
def insertionSort(a):
    numShifts = 0
    for j in range(1, len(a)):  # n - 1 iterations
        key = a[j]   # 1 * (n - 1)
        i = j - 1    # 2 * (n - 1)
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            numShifts += 1
            i -= 1
        a[i + 1] = key
    print('# of shifts:', numShifts)

n = 10000
numbers = []
for i in range(n, 0, -1):
    numbers.append(i)

#print('Before sorting:', numbers)
insertionSort(numbers)
#print('After sorting:', numbers)
