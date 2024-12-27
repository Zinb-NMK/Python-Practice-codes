def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    #Find the midpoint
    mid = len(arr) //2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #Recursively sort both halves
    left_sort = merge_sort(left_half)
    right_sort = merge_sort(right_half)

    #Merge the two sorted halves
    return merge(left_sort, right_sort)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

arr = [49, 45, 67, 2, 34, 10]
sorted_list = merge_sort(arr)
print("Sorted Array: ",sorted_list)