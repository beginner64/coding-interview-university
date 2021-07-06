def quick_sort(arr,start,end):
    if start >=end:
        return 
    partition_index = partition(arr,start,end)
    quick_sort(arr, start, partition_index-1)
    quick_sort(arr, partition_index+1, end)

def partition(arr,start,end):
    pi= start
    pi_element = arr[start]
    arr[end],arr[pi] = arr[pi],arr[end]
    pi=end
    end-=1
    while start<=end:
        while start<=end and  arr[start] <=pi_element:
            start+=1
        while end>=start and  arr[end] >= pi_element:
            end-=1
        if start <=end:
            arr[start],arr[end] = arr[end],arr[start]
    arr[start],arr[pi]=arr[pi],arr[start]
    return start


from random import randrange
arr =  [randrange(1001) for i in range(1001)]
# arr = [4, 6, 5, 2, 0]
# print("programming-language-resources.md",arr)
sorted_arr = sorted(arr)
quick_sort(arr,0,len(arr)-1)
# print("post",arr)
# print(arr)
print(sorted_arr == arr)
# print(arr)