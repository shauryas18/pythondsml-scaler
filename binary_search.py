# Binary Search Program (handles comma & space input)

# Take input and handle both comma and space
a = list(map(int, input("Enter sorted array: ").replace(",", " ").split()))

target = int(input("Enter target: "))

n = len(a)
start = 0
end = n - 1

# Binary Search
while start <= end:
    mid = (start + end) // 2

    if a[mid] == target:
        print("Element found at index:", mid)
        break
    elif a[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
else:
    print("Element not found")