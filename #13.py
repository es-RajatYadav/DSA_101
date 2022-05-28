def findSumPair(array, target):
    hashTable = {}
    for i in array:
        complement = target - i;
        if complement in hashTable:
            hashTable[complement] += 1
            print('Pair found : ({}, {})'.format((target - complement), complement))
        else:
            hashTable[complement] = array.index(i)


print(findSumPair([1, 2, 4, 5, 6, 2, 5], 8))
