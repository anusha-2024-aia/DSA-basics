lst = [15, 14, 12, 9, 7, 6, 5]
target = 7
low = 0
high = len(lst) - 1
pos = -1  # Default: not found

while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target:
        pos = mid  # Found position
        break
    elif lst[mid] < target:  # For descending order
        high = mid - 1
    else:
        low = mid + 1

if pos != -1:
    print(f"Element found at position: {pos}")  # 0-based index
else:
    print("Element not found")
