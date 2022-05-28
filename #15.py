def printSubArrayZero(array):
    for i in range(len(array)):
        tempSum = array[i]
        for j in range(i+1, len(array)):
            tempSum += array[j]
            if tempSum == 0:
                print("Sub-Array : ({}, {})".format(i, j))


printSubArrayZero([1, 2, -3, 3])
