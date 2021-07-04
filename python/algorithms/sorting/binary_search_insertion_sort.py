def binary_search(arr,elem, start,end):
    while start <= end:
        mid = start + ((end-start) //2)
        if elem > arr[mid] :
            start= mid+1
        else:
            end = mid-1
    return start


def binary_search_insert_sort(arr):
    l = len(arr)
    for i in range(1,l):
        elem = arr[i]
        index = binary_search(arr,elem,0,i-1)
        for j in range(i,index,-1):
            arr[j] = arr[j-1]
        arr[index] = elem


from random import randrange
for i in range(1000):
    arr =  [randrange(1000) for i in range(1001)] 
    # arr = [0, 6, 5, 2, 4, 5, 2, 3, 6, 6]
    # ind = binary_search(arr,5,0,1)
    # print(ind)
    # print("programming-language-resources.md",arr)
    sorted_arr = sorted(arr)
    binary_search_insert_sort(arr)
    # print("post",arr)
    if sorted_arr != arr:
        print("failed",arr)
        break 

# print(arr)