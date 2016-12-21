
class LString:

    class LStringNode:
        def __init__(self, nextPtr, charVal):
            self.next = nextPtr
            self.char = charVal

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
            self.last.next = nextNode
            self.last = nextNode
        self.length += 1

    def _getNodeAt(self, index):
        if index == self.length:
            return self.last
        elif index < self.length and index > 0:
            i = 1
            nextNode = self.first
            while i != index:
                nextNode = nextNode.next
                i += 1
            return nextNode

    def _isValidIndex(self, index):
        return (index > 0 and index < self.length)

    def getCharAt(self, index):
        if self._isValidIndex(index):
            return self._getNodeAt(index).char
        else:
            print("Index out of bounds")

    def setCharAt(self, index, char):
        if self._isValidIndex(index):
            self._getNodeAt(index).char = char    
        else: 
            print("Index out of bounds")

    def subStr(self, start, end):
        nextNode = self._getNodeAt(start)
        if nextNode is None:
            print("Invalid start index for substring")

        if end < self.length:
            print("Invalid end index for substring") 

        retStr = ""
        for i in range(start, end):
            retStr += nextNode.char
            nextNode = nextNode.next
        
        return retStr


    def __iter__(self):
        self.tempNext = self.first
        return self 

    def __next__(self):
        if self.tempNext is None:
            raise StopIteration

        retChar  = self.tempNext.char
        self.tempNext = self.tempNext.next
        return retChar 

    def __add__(self, other):
        newLstring = LString()

        for char in self:
            newLstring.addChar(char)

        for char in other:
            newLstring.addChar(char)

        return newLstring

    # add in this case is symetric so this is not needed
    # I might want to use this for concatenation with a str
    def __radd__(self, other):
        newLstring = LString()

        for char in other:
            newLstring.addChar(char)

        for char in self:
            newLstring.addChar(char)

        return newLstring

    def __str__(self):
        retString = ""

        nextNode = self.first
        while nextNode is not None:
            retString += nextNode.char
            nextNode = nextNode.next
        
        return retString

    def __len__(self):
        return self.length

def printAssert(testVal, actualVal): 
    print("The following should be \"" + str(testVal) + "\" : \"" + str(actualVal) + "\"")

testStr = "Here is a string"
testLstring = LString(testStr)

printAssert(len(testStr), len(testLstring))
printAssert(testStr, testLstring)
print()

#Test getCharAt
printAssert("e", testLstring.getCharAt(2))
printAssert("None", testLstring.getCharAt(len(testLstring)))
printAssert("None", testLstring.getCharAt(0))
print()

#Test add
testStr2 = " and another string "
newLstring = testLstring + LString(testStr2)
newLstring2 = LString(testStr2) + testLstring 
printAssert(testStr + testStr2, newLstring) 
printAssert(testStr2 + testStr, newLstring2) 
print()

#Test substring
printAssert(testStr[1:3], testLstring.subStr(1,3)) 

print(newLstring.getCharAt(2))
testLstring.setCharAt(3, "e")
print(testLstring)
print(newLstring.getCharAt(2))

