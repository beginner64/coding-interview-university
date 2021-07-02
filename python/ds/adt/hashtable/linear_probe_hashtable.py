class HashTable(object):
    def __init__(self):
        self.m = 8
        self.arr = [None] * self.m
        self.s = 0
        self.max_load_factor = 0.5
        self.shrink_factor = 0.25
        self.min_size_for_shrink = 8

    def hash(self,k):
        return hash(k)%self.m

    def _increment_hash(self, h):
        return (h+1) % self.m

    def add(self,key,value):
        h = self.hash(key)
        while self.arr[h]!= None and self.arr[h] != '\0':
            if self.arr[h][0] == key:
                self.arr[h] = (key,value)
                return
            h=self._increment_hash(h)
        self.arr[h] = (key,value)
        self.s+=1
        if self.s /self.m >= self.max_load_factor:
            self.resize(1/self.max_load_factor)

    def exists(self,key):
        return self._find_item(key) != None

    def get(self,key):
        index = self._find_item(key)
        return self.arr[index][1]

    def remove(self,key):
        index = self._find_item(key)
        self.arr[index] = '\0' 
        self.s-=1    
        # if (self.m > self.min_size_for_shrink) and (self.s /self.m <= self.shrink_factor):
        #     self.resize(max(self.min_size_for_shrink/self.m, self.shrink_factor))
    
    def _find_item(self,key):
        h = self.hash(key)
        start =h
        while self.arr[h]!= None:
            if self.arr[h][0]== key:
                return h
            else:
                h = self._increment_hash(h)
                if h == start:
                    return None
        return None

    def resize(self,factor):
        self.m = int(self.m * factor)
        print(self.m,"new size")
        arr = self.arr
        self.arr = [None]* self.m
        self.s=0
        for i in arr:
            if i != None and i != '\0':
                self.add(i[0],i[1])

    def print(self):
        print(self.arr)

if __name__ == "__main__":
    obj = HashTable()
    # obj.print()
    obj.add(0,1)
    # obj.print()
    obj.add('a',1)
    # obj.print()
    obj.add('b',2)
    # obj.print()
    obj.add(1,2)
    # obj.print()
    obj.add(2,3)
    # obj.print()
    obj.add(3,4)
    # obj.print()
    obj.add(4,5)
    obj.add(7,8)
    obj.add(9,10)
    obj.print()
    # print(obj.get(1))
    # print(obj.get(3))
    # print(obj.get('a'))
    # print(obj.get('b'))
    # obj.print()
    obj.remove(0)
    obj.remove(1)
    obj.remove('a')
    # obj.remove('b')
    # obj.remove(3)
    obj.print()
    obj.add(9,11)
    # obj.remove()
    obj.print()
    print(obj.s)
    # https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/