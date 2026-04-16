# This program finds all palindrome permutations of a string

from itertools import permutations

A = "aabbaa"

# Step 1: Count frequency
freq = {}
for char in A:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Step 2: Check if palindrome is possible
odd_char = ""
odd_count = 0

for char in freq:
    if freq[char] % 2 == 1:
        odd_count += 1
        odd_char = char

# If more than one odd → no palindrome possible
if odd_count > 1:
    print("No palindrome permutations possible")
else:
    # Step 3: Build half string
    half = ""
    for char in freq:
        half += char * (freq[char] // 2)

    # Step 4: Generate unique permutations of half string
    unique_perms = set(permutations(half))

    result = []

    # Step 5: Form full palindrome
    for perm in unique_perms:
        half_str = "".join(perm)
        if odd_count == 1:
            palindrome = half_str + odd_char + half_str[::-1]
        else:
            palindrome = half_str + half_str[::-1]
        result.append(palindrome)

    # Print result
    print("Palindrome permutations:")
    for p in result:
        print(p)