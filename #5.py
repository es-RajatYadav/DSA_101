# def findTargetEle(array, tar):
#     for i in range(len(array)):
#         for j in range(1, len(array)):
#             if int(array[i]) + int(array[j]) == tar:
#                 print("Found at {} {}".format(i, j))
#                 break
#
#
# target = int(input('Enter target : '))
# inputArray = input('Enter Array : ')
# findTargetEle(list(inputArray), target)

# Via Hash Table

def findTargetEle(array, tar):
    hashTable = {}
    for i in array:
        complement = tar - i;
        if complement in hashTable:
            print("Pair found")
            break
        else:
            hashTable[i] = array.index(i)
    print(hashTable)


findTargetEle([1, 2, 3], 4)
