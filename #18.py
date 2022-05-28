def duplicateElement(array, x, y):
    hashTable = {}
    for i in range(x, y):
        if array[i] in hashTable:
            hashTable[array[i]] += 1
        else:
            hashTable[array[i]] = 1

    for i in hashTable:
        if hashTable[i] > 1:
            print("Duplicate element found.")


duplicateElement([1, 2, 3, 4, 2, 1, 6], 1, 7)
