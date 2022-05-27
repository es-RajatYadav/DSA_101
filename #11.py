class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    @staticmethod
    def hashAlgorithm(self, key):
        hashCode = 0
        for i in range(len(key)):
            hashCode = (hashCode + key.charCodeAt(i)) * i % len(self.data)

        return hashCode

    @staticmethod
    def setEle(self, key):
        address = self.hashAlgorithm(key)
        if not self.data[address]:
            self.data[address] = []
            self.data[address].append([key])
        print(self.data)


h1 = HashTable(50)
h1.setEle('Rajah', 10000)
