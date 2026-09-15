arr = [2,34,56,78,90,12,431]
target = int(input("Enter the element to search : "))

left = 0
right = len(arr) - 1
result = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        result = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")