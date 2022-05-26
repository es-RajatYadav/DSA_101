def mergeList(list1, list2):
    i = 0
    j = 0
    k = 0
    mergedList = [None] * (len(list1) + len(list2))
    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            mergedList[k] = list1[i]
            k += 1
            i = i + 1
        else:
            mergedList[k] = list2[j]
            k += 1
            j = j + 1

    while i < len(list1):
        mergedList[k] = list1[i]
        k += 1
        i = i + 1

    while j < len(list2):
        mergedList[k] = list2[j]
        k += 1
        j = j + 1

    return mergedList


print(mergeList([1, 3, 5, 7], [2, 4, 6, 8]))
