class BinHeap:
    def __init__(self, maxSize):
        self.heapList = [0]
        self.currentSize = 0
        self.maxSize = maxSize

    def __str__(self):
        return str(self.heapList[1::])

    def __len__(self):
        return len(self.heapList[1::])

    def size(self):
        return self.currentSize

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        if self.currentSize + 1 > self.maxSize:
            self.delMin()
            self.heapList.append(k)
            self.currentSize += 1
        else:
            self.heapList.append(k)
            self.currentSize += 1
            self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


bh = BinHeap(6)
bh.buildHeap([9, 5, 6, 2, 3])

print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('DEL MIN - ', bh.delMin())
print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('INSERT 10')
bh.insert(10)
print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('INSERT 20')
bh.insert(20)
print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('INSERT 30')
bh.insert(30)
print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('INSERT 11')
bh.insert(11)
print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('INSERT 12')
bh.insert(12)
print('HEAP - ', bh)
print('LEN - ', len(bh))
print('SIZE - ', bh.size())

print('='*90)

print('INSERT 13')
bh.insert(13)
print('HEAP - ',bh)
print('LEN - ',len(bh))
print('SIZE - ',bh.size())