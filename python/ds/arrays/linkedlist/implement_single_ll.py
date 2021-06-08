class SingleLLNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class SingleLLWithoutTail(LinkedList):
    def __init__():
        self.head = None
        self.size = 0 
    def size(self):
        return self.size

    def empty(self):
        return self.size ==0
    def value_at(self,index):
        if index >= size:
            raise Exception("index is greater than size")
        tmp = self.head
        tmp_index = 0
        while index !=tmp_index:
            tmp= tmp.next
            tmp_index+=1 
        return tmp.value

    def push_front(self,value):
        node = SingleLLNode(value)
        node.next = self.head
        self.head = node
        self.size+=1

    def pop_front(self,value):
        if(self.empty()):
            print("not data exist")
        else:
            value = self.head.value
            self.head = self.head.next
            self.size-=1
            return value

    def push_back(self,value):
        node = SingleLLNode(value)
        if(self.empty()):
            self.head =  node
        else:
            tmp=self.head
            while(tmp.next is not None):
                tmp = tmp.next
            tmp.next = node
        self.size+=1

    def pop_back(self,value):
        if(self.empty()):
            print("not data exist")
        else:
            if self.size ==1:
                value = self.head.value
                self.head = None
            else:
                tmp=self.head
                while(tmp.next.next is not None):
                    tmp = tmp.next
                value = tmp.next.value
                tmp.next = None
            self.size-=1
            return value

    def front(self):
        if (self.empty()):
            print("not data exist")
        else:
            return self.head.value
    def back(self):
        if (self.empty()):
            print("not data exist")
        else:
            tmp=self.head
            while(tmp.next is not None):
                tmp = tmp.next
            return tmp.value
    def insert(self,index,value):
        raise Exception('not implemented')
    def erase(self,index):
        raise Exception('not implemented')
    def value_n_from_end(self,n):
        raise Exception('not implemented')
    def reverse(self):
        raise Exception('not implemented')
    def remove_value(self,value):
        raise Exception('not implemented')