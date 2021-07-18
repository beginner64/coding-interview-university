class MaxHeap(object):
    def __init__(self,size):
            self.heap=[]
            self.s=0

    def insert(self,elem):
        self.heap.append(elem)
        self.s+=1
        self.shift_up()

    def shift_up(self):
        index = self.s-1
        while self.heap[index //2] < self.heap[index]:
            self.heap[index //2],self.heap[index] = self.heap[index],self.heap[index //2]
            index =index //2
                    
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
            self.shift_down()
            return max_elem
        else:
            return None

    def shift_down(self):
        index = 1
        while True:
            left_index = 2 * index -1
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



    def heapify(self,arr):
        ...


    def heap_sort(self,arr):
        arr = self.heapify(arr)
        

    def remove(self,i):
        ...
if __name__ == "__main__":
    ...

