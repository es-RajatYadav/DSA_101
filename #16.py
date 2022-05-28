def sortBinaryArray(array):
    hashTable = {}
    for i in array:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    print(hashTable)
    sortedArray = '0' * hashTable[0] + '1' * hashTable[1]
    return list(sortedArray)


print(sortBinaryArray([1, 0, 1, 1, 0, 0, 0]))
