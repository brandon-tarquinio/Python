
class LString:

    class LStringNode:
        def __init__(self, nextPtr, charVal):
            self.next = nextPtr
            self.char = charVal

        def getNext(self):
            return self.next

        def getChar(self):
            return self.char

        def setNext(self, nextPtr):
            self.next = nextPtr

        def setChar(self, char):
            self.char = char

    def __init__(self, initString=""):
        self.first = None
        self.length = 0

        for char in initString:
            self.addChar(char)

    def addChar(self, char):
        if self.first is None:
            self.first = self.LStringNode(None, char)
            self.last = self.first
        else:
            nextNode = self.LStringNode(None, char)
            self.last.setNext(nextNode)
            self.last = nextNode
        self.length += 1

    def _getNodeAt(self, index):
        if index == self.length:
            return self.last
        elif index < self.length and index > 0:
            i = 1
            nextNode = self.first
            while i != index:
                nextNode = nextNode.getNext() 
                i += 1
            return nextNode

    def getCharAt(self, index):
        #if index > self.length or index < 0:
        if index > 0 and index < self.length: 
            return self._getNodeAt(index).getChar()
        else:
            print("Index out of bounds")

    def setCharAt(self, index, char):
        if index > 0 and index < self.length: 
            self._getNodeAt(index).setChar(char)     
        else: 
            print("Index out of bounds")

    def __add__(self, other):
        newLstring = LString()
        newLstring.first = self.first
        newLstring.last = self.last
        return newLstring

    def __radd__(self, other):
        print("Im here") 

    def __str__(self):
        retString = ""

        nextNode = self.first
        while nextNode is not None:
            retString += nextNode.getChar()
            nextNode = nextNode.getNext()
        
        return retString

    def __len__(self):
        return self.length


testLstring = LString("Here is a string")
print(len(testLstring))
print(testLstring)

#Test add
newLstring = testLstring + LString("blah")
print(newLstring.getCharAt(2))
testLstring.setCharAt(3, "e")
print(testLstring)
print(newLstring.getCharAt(2))

#Test getCharAt
print(testLstring.getCharAt(2))
print(testLstring.getCharAt(len(testLstring)))
print(testLstring.getCharAt(0))
