L = [12, 45, 7, 23, 89, 34, 5]

print("Original list:", L)

count = 0

for num in L:
    count += num

avg = count / len(L)

print("Sum:", count)
print("Average:", avg)

L.sort()

print("Sorted list:", L)
print("Smallest element:", L[0])
print("Largest element:", L[-1])