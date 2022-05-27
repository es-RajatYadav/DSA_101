def find1stRe(array):
    hashTable = {}
    for i in array:
        if i in hashTable:
            return i
        else:
            hashTable[i] = array.index(i)


if not find1stRe([1, 2, 4, 5, 6, 1]):
    print("No Element found.")
else:
    print(find1stRe([1, 2, 4, 5, 6, 1]))
