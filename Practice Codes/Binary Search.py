def binarysearch(arr, target):
    left, right = 0, len(arr) - 1 #Left and Right Positions

    while left <= right:
        mid = (left + right )//2 #Find Mid element

        if arr[mid] == target: #Target is in mid
            return mid

        elif arr[mid] < target:
            left = mid + 1 #Target is in right half

        else:
            right = mid - 1 #Target is in left hal

    return -1 #Target found
arr = list(map(int,input("Enter a sorted array of integers(seperated by space.):").split()))
target = int(input("Enter Target value: "))
result = binarysearch(arr, target)

if result != 1:
    print(f"Target found at index: {result}")
else:
    print("Target not found in the list")