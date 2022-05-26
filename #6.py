# Via hash table
def findSubArray(array):
    allSums = 0
    hashTable = {}
    i = 0
    startPoint = 0

    while startPoint < len(array):
        while i < len(array):
            indexString = ''+str(i)
            allSums += array[i]
            hashTable[indexString] = allSums
            i += 1
        startPoint += 1

    print(hashTable)


findSubArray([1, 2, 4, 5, 6, -8, 1, 5])
