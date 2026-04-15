# This program checks whether a string can be rearranged to form a palindrome

A = "aabbaa"   

freq = {}      # Dictionary to store frequency of each character

# Step 1: Count frequency of each character
for char in A:
    if char in freq:
        freq[char] += 1   # Increase count if character already exists
    else:
        freq[char] = 1    # Initialize count as 1 if new character

# Step 2: Count how many characters have odd frequency
odd_frequencies = 0

for frequency in freq.values():   # Loop through all frequency values
    if frequency % 2 == 1:        # Check if frequency is odd
        odd_frequencies += 1      # Increase odd count

# Step 3: Check palindrome condition
if odd_frequencies <= 1:
    print(1)   # Palindrome 
else:
    print(0)   # Palindrome not