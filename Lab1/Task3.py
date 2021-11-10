def prime(n):
    np = []
    isprime = []
    for i in range(n + 1, n + 200):
        np.append(i)
    for j in np:
        val_is_prime = True
        for x in range(2, j - 1):
            if j % x == 0:
                val_is_prime = False
                break
        if val_is_prime:
            isprime.append(j)
    return min(isprime)


def before(n):
    np = []
    isprime = []
    for i in range(1, n - 1):
        np.append(i)
    for j in np:
        val_is_prime = True
        for x in range(2, j - 1):
            if j % x == 0:
                val_is_prime = False
                break
        if val_is_prime:
            isprime.append(j)
    return max(isprime)


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def apdate(self):
        slot = self.slots
        dat = self.data
        self.slots = [None] * self.size
        self.data = [None] * self.size
        for i in range(len(slot)):
            if slot[i] != None:
                self.put(slot[i], dat[i])

    def put(self, key, data):
        if (len(self) / self.size) > 0.7:
            print(len(self) / self.size)
            pr = prime(self.size)
            self.size += pr
            self.apdate()
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        sum = 0
        for i in range(len(key)):
            z = ord(key[i])
            sum += z * i
        return sum % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        s = 0
        for i in self.data:
            if i != None:
                s += 1
        return s

    def __contains__(self, item):
        for i in range(self.size):
            if self.data[i] == item:
                return True
        return False

    def __delitem__(self, key):
        if (len(self) / self.size) < 0.2:
            pr = self.size - before(self.size)
            self.size -= pr
            self.apdate()
        self.data[key % self.size] = None
        self.slots[key % self.size] = None


H = HashTable()
H["54"] = "cat"
H["26"] = "dog"
H["93"] = "lion"
H["17"] = "tiger"
H["77"] = "bird"
H["31"] = "cow"
H["44"] = "goat"
H["55"] = "pig"
print(H.slots)
print(H.data)
H["20"] = "chicken"
print(H.slots)
print(H.data)

print(H["20"])

print(len(H))

print("lion" in H)

print(H["17"])
H["20"] = 'duck'
print(H["20"])

print(H["20"])
print(H["99"])

H.put("75", "sat")
print(H.slots)
print(H.data)
