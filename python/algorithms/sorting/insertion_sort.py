
def insert_sort(arr):
    l = len(arr)
    for next_elem_ind in range(1,l):
        # print(arr,list(range(0,next_elem_ind)))
        for prev_elem_ind in range(next_elem_ind-1,-1,-1):
            print(arr[prev_elem_ind] > arr[next_elem_ind],arr,arr[prev_elem_ind],arr[next_elem_ind],list(range(next_elem_ind-1,-1,-1)))
            if arr[prev_elem_ind] > arr[next_elem_ind]:
                arr[next_elem_ind],arr[prev_elem_ind]= arr[prev_elem_ind],arr[next_elem_ind]
            # else:
                #     break
        print("loop",arr,next_elem_ind,prev_elem_ind)





from random import randrange
# arr =  [randrange(100) for i in range(101)]
arr = [0, 6, 5, 2, 4]
# print("programming-language-resources.md",arr)
sorted_arr = sorted(arr)
insert_sort(arr)
# print("post",arr)
print(sorted_arr == arr)
# print(arr)