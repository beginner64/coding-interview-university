from python.ds.linkedlist.implement_single_ll_without_tail import SingleLLWithoutTail
from python.ds.linkedlist.interface_ll import SingleLLNode

class SingleLLWithTail(SingleLLWithoutTail):
    def __init__(self):
        self.head = None
        self.size = 0 
        self.tail = None

    def push_front(self,value):
        node = SingleLLNode(value)
        node.next = self.head
        self.head = node
        if(self.empty()):
            self.tail = node
        self.size+=1

    def pop_front(self):
        if(self.empty()):
            print("no data exist")
        else:
            value = self.head.value
            self.head = self.head.next
            self.size-=1
            if(self.empty()):
                self.tail = None
            return value

    def push_back(self,value):
        node = SingleLLNode(value)
        if(self.empty()):
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size+=1

    def pop_back(self):
        if(self.empty()):
            print("no data exist")
        else:
            if self.size ==1:
                value = self.head.value
                self.head = None
                self.tail = None
            else:
                tmp=self.head
                while(tmp.next.next is not None):
                    tmp = tmp.next
                value = tmp.next.value
                tmp.next = None
                self.tail = tmp
            self.size-=1
            return value

    def back(self):
        if (self.empty()):
            print("no data exist")
        else:
            return self.tail.value

    def insert(self,index,value):
        #  insert value at index, so current item at that index is pointed to by new item at index
        self.check_index(index,offset=1)
        if index ==0:
            self.push_front(value)
            return
        if index == self.size:
            self.push_back(value)
            return
        node = SingleLLNode(value)
        tmp = self.head
        tmp_index = 0
        while index-1 !=tmp_index:
            tmp= tmp.next
            tmp_index+=1 
        node.next= tmp.next      
        tmp.next = node
        self.size+=1

    def erase(self,index):
        # removes node at given index
        self.check_index(index)
        if index ==0:
            self.pop_front()
            return
        if index == self.size:
            self.pop_back()
            return
        tmp = self.head
        tmp_index = 0
        while index-1 !=tmp_index:
            tmp= tmp.next
            tmp_index+=1
        tmp.next = tmp.next.next
        self.size-=1
        
    def reverse(self):
        self.tail = self.head
        cur = self.head
        prev = None
        while cur != None:
            stor = cur.next
            cur.next = prev
            prev = cur
            cur = stor
        self.head = prev

    def remove_value(self,value):
        if value == self.head.value:
            self.pop_front()
            return
        if value == self.tail.value:
            self.pop_back()
            return
        tmp = self.head
        while(tmp.next != None and tmp.next.value !=value):
            tmp = tmp.next
        if(tmp.next==None):
            return f"{value} value does not exist"
        else:
            tmp.next = tmp.next.next
        self.size-=1

if __name__ == "__main__":
    obj = SingleLLWithTail()
    print(obj.size)
    print(obj.front())
    print(obj.back())    
    obj.pop_front()
    obj.pop_back()
    obj.push_front(1)
    obj.push_front(2)
    print(obj.back())
    obj.print()
    obj.push_back(3)
    obj.push_back(4)
    obj.print()
    obj.push_front(5)
    obj.print()
    print(obj.size)
    print(obj.front())
    obj.pop_front()
    obj.print()
    obj.pop_back()
    obj.print()
    obj.push_front(5)
    obj.print()
    obj.push_back(4)
    print(obj.front())
    print(obj.back())
    obj.print()
    obj.reverse()
    obj.print()
    print(obj.front())
    print(obj.back())
    obj.insert(0, 10)
    obj.insert(5, 12)
    obj.insert(7, 11)
    obj.print()
    obj.erase(0)
    obj.erase(4)
    obj.print()
    obj.remove_value(5)
    obj.print()
    obj.remove_value(1)
    obj.print()
    obj.remove_value(4)
    obj.print()
    obj.push_front(5)
    obj.push_front(1)
    obj.print()
    obj.reverse()
    obj.print()
    obj.pop_back()
    obj.pop_back()
    obj.print()
    obj.reverse()
    obj.print()
    obj.pop_back()
    obj.reverse()
    obj.print()
    obj.reverse()
    obj.print()
    obj.pop_back()
    obj.print()
    obj.push_front(20)
    obj.push_front(4)
    obj.push_front(15)
    obj.push_front(35)
    obj.print()
    print(obj.value_n_from_end(2))
