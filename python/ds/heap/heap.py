# heap python implementation heap sort
class MaxHeap(object):
    def __init__(self):
            self.heap=[]
            self.s=0

    def insert(self,elem):
        print("inserting elem",elem)
        self.heap.append(elem)
        self.s+=1
        self.shift_up()


    def get_parent_index(self,ind):
        return (ind-1)//2

    def shift_up(self):
        index = self.s-1
        while self.heap[self.get_parent_index(index)] < self.heap[index] and index >0:
            self.heap[self.get_parent_index(index)],self.heap[index] = self.heap[index],self.heap[self.get_parent_index(index)]
            index =self.get_parent_index(index)
                    
    def get_max(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            return None

    def get_size(self):
        return self.s

    def is_empty(self):
        return self.s ==0

    def extract_max(self):
        if not self.is_empty():
            max_elem = self.heap[0]
            self.heap[0]= self.heap[-1]
            self.s-=1
            self.shift_down(0)
            del self.heap[-1]
            return max_elem
        else:
            return None

    def shift_down(self,index):
        while True:
            left_index = 2 * index+1
            right_index = left_index+1
            if left_index < self.s and right_index <self.s:
                max_index =  left_index if self.heap[left_index] > self.heap[right_index] else right_index
            elif left_index < self.s:
                max_index = left_index
            elif right_index <self.s:
                max_index=right_index
            else:
                break
            if self.heap[index] < self.heap[max_index]:
                self.heap[index],self.heap[max_index] = self.heap[max_index],self.heap[index]
                index = max_index
            else:
                break

    def heapify(self,arr,s,ind):
        self.heap=arr
        self.s=s
        for index  in range(ind,-1,-1):
            self.shift_down(index)
        return self.heap


    def heap_sort(self,arr):
        self.heapify(arr,len(arr),(self.s-1) //2 )
        i = len(arr)-1
        while i>=0:
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,self.s-1,(self.s-1) //2 )
            i-=1

    def remove(self,i):
        # https://www.geeksforgeeks.org/insertion-and-deletion-in-heaps/
        self.heap[i] = self.heap[self.s-1]
        self.heapify(self.heap,self.s-1,i)

    def print(self):
        print(self.heap[0:self.s])

if __name__ == "__main__":
    maxHeap = MaxHeap()
    arr =[5,3,17,10,84,19,6,22,9]
    for i in arr:
        maxHeap.insert(i)
    maxHeap.print()
    data= maxHeap.heap[:]
    while maxHeap.heap:
        print(maxHeap.extract_max())
    maxHeap.heapify(arr,len(arr),(len(arr)-1) //2)
    maxHeap.print()
    while maxHeap.heap:
        print(maxHeap.extract_max())
    arr = [91,91,82,73,64,55,46,37,28,28,19,10,10]
    print("heap sort")
    maxHeap.heap_sort(arr)
    print(arr)
    arr =[5,3,17,10,84,19,6,22,9]
    maxHeap.heap=[]
    for i in arr:
        maxHeap.insert(i)
    maxHeap.print()
    maxHeap.remove(0)
    maxHeap.remove(2)
    maxHeap.print()
