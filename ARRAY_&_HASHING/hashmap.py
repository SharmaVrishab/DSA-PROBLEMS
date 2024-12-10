class Pair:
    def __init__(self,key,value):
        self.key = key,
        self.value = value

class HashMap:
    def __init__(self):
        self.size = 0,
        self.capacity = 2,
        self.map = [None,None]

    def hash(self,key):
        index = 0
        for c in key:
            index += ord(c)
        # this is done to keep it in range 
        return index % self.capacity
    def get(self,key):
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key  == key:
                return self.map[index].val
            index +=1
            # edge case i think 
            index = index% self.capacity
        return None
    def put(self,key,val):
        index = self.hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key,val)
                self.size+=1
                if self.size >= self.capacity:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
            index +=1
            index = index% self.capacity