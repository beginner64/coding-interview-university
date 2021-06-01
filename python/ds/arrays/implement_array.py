class Array(object):
    def __init__(self,size,default_value=0):
        self.capacity = 10
        while True:
            if size >= self.capacity:
                self.capacity = 2 * self.capacity
            else:
                break
        self.size=size        
        self.arr = []
        for i in range(self.capacity):
            self.arr.append(default_value)
        self.default_value=default_value
    
    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def check_index_range(self,index):
        if index < 0 or index >= self.capacity:
            raise  Exception("range error")
    def at(self,index):
        self.check_index_range(index)
        return self.arr[index]
    def push(self,value):
        if self.size >= self.capacity:
            self._resize()
        self.arr[self.size]=value
        self.size+=1
    def insert(self,index,value):
        if self.size >= self.capacity:
            self._resize()
        for ind in range(self.size,index,-1):
            self.arr[ind]= self.arr[ind-1]
        self.arr[index]=value
        self.size+=1
    
    def prepend(self,value):
        self.insert(0, value)
    
    def pop(self):
        if not self.is_empty():
            value = self.arr[self.size-1]
            self.arr[self.size-1]=self.default_value
            self.size-=1
            return value

    def delete(self,index):
        self.check_index_range(index)
        for ind in range(index,self.size):
            self.arr[ind]= self.arr[ind+1]
        self.arr[self.size]=self.default_value
        self.size-=1

    def remove(self,value):
        while True:
            index = self.find(value)
            if index !=-1:
                self.delete(index)
            else:
                break

    def find(self,value):
        for ind in range(self.size):
            if self.arr[ind] == value:
                return ind
        return -1
    def _resize(self):
        old_capacity = self.capacity
        self.capacity = self.capacity * 2 
        print("increasing capacity to ", self.capacity)
        for i in range(old_capacity,self.capacity):
            self.arr.append(self.default_value)

arr = Array(10)
for i in range(20):
    arr.push(1)
arr.remove(1)
arr.push(2)
arr.insert(1, 20)
print(arr.arr)
arr.delete(1)
print(arr.arr)