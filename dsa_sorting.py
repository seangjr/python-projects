def binary_search(arr, query):
    position = 0
    while True:
        if arr[position] == query:
            return position
        position += 1
        if position == len(arr):
            return -1

arr = [0, 12, 34, 9, 33, 2]
print(f"Original array: {arr}")
print(f"Binary Search: Position {binary_search(arr, 2)}")

def bubble_sort(arr):
    swapped = False
    i = 0
    while i < len(arr) and swapped:
        swapped = False
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
            i += 1
    return arr

print(bubble_sort(arr))
