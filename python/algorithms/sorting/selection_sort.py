def select_sort(arr):
    l = len(arr)
    for i in range(l-1):
        min_index=i
        for j in range(i+1,l):
            if arr[j] <  arr[min_index]:
                min_index =j
        arr[i],arr[min_index] = arr[min_index],arr[i]

from random import randrange
arr =  [randrange(10) for i in range(101)]
# arr = [0, 6, 5, 2, 4]
# print("programming-language-resources.md",arr)
sorted_arr = sorted(arr)
select_sort(arr)
# print("post",arr)
print(sorted_arr == arr)
# print(arr)
