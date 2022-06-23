class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextPtr = None


class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def prepend(self, data=None):
        newNode = Node(data)
        temp = self.head
        self.head = newNode
        newNode.nextPtr = temp
        self.count += 1
        if self.count == 1:
            self.tail = self.head

    def append(self, data=None):
        newNode = Node(data)
        if self.count == 0:
            self.head = newNode
        else:
            self.tail.nextPtr = newNode
        self.tail = newNode
        self.count += 1

    def removeAtFirst(self):
        if self.count > 0:
            self.head = self.head.nextPtr
            self.count -= 1
            if self.count == 0:
                self.tail = None

    def removeAtEnd(self):
        if self.count > 0:
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.nextPtr != self.tail:
                    current = current.nextPtr
                current.nextPtr = None
                self.tail = current
                self.count -= 1

    def remove(self, searchvalue):
        previous = None
        current = self.head
        while current is not None:
            if current.data == searchvalue:
                if previous is not None:
                    previous.nextPtr = current.nextPtr
                    if current.nextPtr is None:
                        self.tail = previous
                    self.count -= 1
                else:
                    self.removeAtFirst()
                return True
            previous = current
            current = current.nextPtr

    def insert(self, prevdata, data):
        newNode = Node(data)
        current = self.head
        while current is not None:
            if current.data == prevdata:
                temp = current.nextPtr
                current.nextPtr = newNode
                newNode.nextPtr = temp
                if current.nextPtr is None:
                    self.tail = newNode
                self.count += 1
                return True
            current = current.nextPtr

    def enumerate(self):
        current = self.head
        while current is not None:
            # Passing values with yield makes this a generator.
            print(current.data)
            current = current.nextPtr


lL = LinkedList()
lL.append('Mon')
lL.append('Tue')
lL.append('Wed')
lL.append('Thurs')
lL.remove('Tue')
lL.insert('Mon', 'Tue')
lL.remove('Wed')
lL.insert('Tue', 'Wed')
lL.enumerate()
