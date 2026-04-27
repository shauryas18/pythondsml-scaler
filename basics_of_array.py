arr = [10, 20, 30, 40]
print(arr[0])   
print(arr[2])   
print(arr[-1])  

arr[1] = 25
print(arr)   # [10, 25, 30, 40]
for i in arr:
    print(i)
    # append and insert
arr.append(50)  
      # add at end → [10,20,30,40,50]
arr.insert(1, 15)     # insert at index 1 → [10,15,20,30,40,50]

arr.remove(30)   # removes value 30
arr.pop()        # removes last element
arr.pop(1)       # removes element at index 1

arr[2] = 100
print(arr)


print(len(arr))

arr.sort()              # ascending
arr.sort(reverse=True)  # descending

print(arr[1:4])   # elements from index 1 to 3

# Concatenation
a = [1, 2, 3]
b = [4, 5]

c = a + b
print(c)   # [1, 2, 3, 4, 5]

# Repetition
arr = [1, 2]
print(arr * 3)   # [1, 2, 1, 2, 1, 2]

# Membership:Checks whether an element exists inside a collection
arr = [10, 20, 30]
print(20 in arr)      # True
print(50 not in arr)  # True

# Identity Operator:Checks whether two variables refer to the SAME object in memory
a = [1, 2, 3]
b = a
print(a is b)   # True (same memory location)


# Built-in Functions
arr = [5, 2, 9, 1]

print(max(arr))   # 9
print(min(arr))   # 1
print(sum(arr))   # 17


# List Comprehension
arr = [1, 2, 3, 4]

new_arr = [x*x for x in arr]
print(new_arr)   # [1, 4, 9, 16]

# Nested Arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])   # 6