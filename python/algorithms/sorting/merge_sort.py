
def merge_sort(arr,start,end):
    if start < end:
        mid = (start + end)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr,start,mid,end)

def merge(arr,start,mid,end):
    new_list =[]
    i=start
    j=mid+1
    # k=start
    # print("pre",arr,arr[start:end+1])
    while i <=mid and j <=end:
        if arr[i] > arr[j]:
            # new_arr[k] = arr[j]
            new_list.append( arr[j])
            j+=1
        else:
            new_list.append( arr[i])
            i+=1
        # k+=1
    while i<=mid:
        new_list.append( arr[i])
        # new_arr[k] = arr[i]
        i+=1
        # k+=1
    while j <=end:
        new_list.append( arr[j])
        # new_arr[k] = arr[j]
        j+=1
        # k+=1
    k=0        
    for i in new_list:
        arr[start+k] = i 
        k+=1
    # arr = new_arr
    # print(arr,arr[start:end+1])






from random import randrange
arr =  [randrange(1000) for i in range(1001)]
# arr = [0, 6, 5, 2, 4]
arr
# print("programming-language-resources.md",arr)
sorted_arr = sorted(arr)
merge_sort(arr,0,len(arr)-1)
# print("post",arr)
print(sorted_arr == arr)
# print(arr)