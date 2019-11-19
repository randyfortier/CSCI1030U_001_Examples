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

def fractionalKnapsack(items, capacity):
    # if there are no items, we cannot carry anything
    if len(items) < 1:
        return []

    # if we have no space, we cannot carry anything
    if capacity == 0:
        return []

    # choose the next best item (highest value)
    bestIndex = 0
    for i in range(len(items)):
        if items[i][1] > items[bestIndex][1]:
            bestIndex = i

    # determine how much of that item we can carry
    if capacity >= items[bestIndex][2]:
        # we can carry it all
        carry = items[bestIndex][0], items[bestIndex][2]
        capacity -= items[bestIndex][2]
        items = items[0:bestIndex] + items[bestIndex + 1:]
        return fractionalKnapsack(items, capacity) + [carry]
    else:
        # we can carry some, and fill our knapsack
        carry = items[bestIndex][0], capacity
        return [carry]

print('Knapsack:', fractionalKnapsack([('diamonds',11,8),('gold',5,13),('silver',3,6)], 20))
print('Knapsack:', fractionalKnapsack([('diamonds',11,8),('gold',5,13),('silver',3,6)], 25))
