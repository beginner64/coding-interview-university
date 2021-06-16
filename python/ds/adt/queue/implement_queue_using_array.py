from python.ds.adt.queue.interface_queue import Queue

class QueueUsingArray(Queue):
    def __init__(self,length):
        self.arr = [0] * length 
        self.head = -1
        self.tail = -1
        self.size = 0
    
    def enqueue(self,value):

        
    
    def dequeue(self):
        
    
    def empty(self):
        return self.lst.empty()

    # def print(self):
        

if __name__ == "__main__":
    queue = QueueUsingLinkedList()  
    queue.enqueue(1)
    queue.enqueue(2)
    # queue.print()
    queue.dequeue()
    queue.dequeue()
    # queue.print()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    # queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(4)
    # queue.print()

