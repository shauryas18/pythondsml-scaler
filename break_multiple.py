#Find second multiple of 7
count = 0

for i in range(1, 101):
    if i % 7 == 0:
        count += 1
        if count == 2:
            print("Second multiple of 7:", i)
            break