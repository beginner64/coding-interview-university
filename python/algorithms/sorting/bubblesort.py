def bubble_sort(arr):
    l = len(arr)
    for index in range(l-1):
        for ind in range(0,l-index-1):
            if arr[ind] > arr[ind+1]:
                arr[ind],arr[ind+1] = arr[ind+1],arr[ind]
            # print(arr,ind)
    return arr

# Optimized Implementation: 
# The above function always runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if inner loop didn’t cause any swap. 
def optimised_bubble_sort(arr):
    l = len(arr)
    for index in range(l-1):
        swap = True
        for ind in range(0,l-index-1):
            if arr[ind] > arr[ind+1]:
                arr[ind],arr[ind+1] = arr[ind+1],arr[ind]
                swap=False
        if swap:
            return
            # print(arr,ind)
    # return arr


from random import randrange
arr =  [randrange(100) for i in range(101)]
# arr = [0, 6, 5, 2, 4, 5, 2, 3, 6, 6]
# print("programming-language-resources.md",arr)
sorted_arr = sorted(arr)
optimised_bubble_sort(arr)
# print("post",arr)
print(sorted_arr == bubble_sort(arr))
# print(arr)