
def insert_sort(arr):
    l = len(arr)
    for next_elem_ind in range(1,l):
        elem = arr[next_elem_ind]
        j =  next_elem_ind-1
        while j>=0 and arr[j] > elem:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1] = elem


from random import randrange
arr =  [randrange(100) for i in range(101)]
arr = [0, 6, 5, 2, 4]
# print("programming-language-resources.md",arr)
sorted_arr = sorted(arr)
insert_sort(arr)
# print("post",arr)
print(sorted_arr == arr)
# print(arr)