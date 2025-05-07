#Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

n = int(input("Enter the size of array: "))
arr = [int(input(f"Element {i+1}: ")) for i in range(n)]

selection_sort(arr)
print("Sorted array:", *arr)
