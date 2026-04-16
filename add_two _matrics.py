# Given matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

# Using map() for addition
C = list(map(lambda row1, row2: 
             list(map(lambda x, y: x + y, row1, row2)), A, B))

# Print result
print("Resultant Matrix:")
for row in C:
    print(row)


#     map(lambda row1, row2: ..., A, B)
# Takes one row from A and one row from B at the same time

# Example:

# row1 = [1, 2, 3]
# row2 = [7, 8, 9]
# 2. Inner map()
# map(lambda x, y: x + y, row1, row2)
# Adds elements of the two rows one by one

# Example:

# x=1, y=7 → 8
# x=2, y=8 → 10
# x=3, y=9 → 12




# #take input by user
# rows = int(input("Enter rows: "))
# cols = int(input("Enter cols: "))

# print("Enter first matrix:")
# A = [list(map(int, input().split())) for _ in range(rows)]

# print("Enter second matrix:")
# B = [list(map(int, input().split())) for _ in range(rows)]

# # Addition using map
# C = list(map(lambda r1, r2: list(map(lambda x, y: x + y, r1, r2)), A, B))

# print("Result:")
# for row in C:
#     print(row)