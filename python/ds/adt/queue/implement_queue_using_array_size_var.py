from python.ds.adt.queue.interface_queue import Queue

class QueueUsingArray(Queue):
    def __init__(self,length):
        self.arr = [0] * length 
        self.head = -1
        self.tail = -1
        self.size = 0
        self.length =length
    
    def enqueue(self,value):
        if self.full():
            print("queue is full")
            return
        if self.empty():
            self.head = 0
            self.tail =0
            self.arr[self.tail] = value
        else:
            self.tail = (self.tail+ 1) % self.length
            self.arr[self.tail] = value
        self.size+=1
        
    
    def dequeue(self):
        if self.empty():
            print("queue is empty")
            return        
        data = self.arr[self.head]
        if self.head == self.tail :
            self.head =-1
            self.tail = -1
        else:
            self.head = (self.head+1)  % self.length
        self.size-=1
        return data
    
    def empty(self):
        return self.size == 0 
    def full(self):
        return self.size == self.length

    def print(self):
        tmp = self.head
        size = self.size
        a=[]
        while size >0:
            a.append(self.arr[tmp])
            tmp= (tmp+1)  % self.length
            size-=1
        print(a)
        

if __name__ == "__main__":
    queue = QueueUsingArray(4)  
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.print()
    queue.enqueue(1)
    queue.print()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.print()

