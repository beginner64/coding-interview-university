from python.ds.linkedlist.implement_single_ll_with_tail import SingleLLWithTail
from python.ds.adt.queue.interface_queue import Queue

class QueueUsingLinkedList(Queue):
    def __init__(self):
        self.lst = SingleLLWithTail()
    
    def enqueue(self,value):
        self.lst.push_back(value)
    
    def dequeue(self):
        self.lst.pop_front()
    
    def empty(self):
        return self.lst.empty()

    def print(self):
        self.lst.print()

if __name__ == "__main__":
    queue = QueueUsingLinkedList()  
    queue.enqueue(1)
    queue.enqueue(2)
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.print()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print()

