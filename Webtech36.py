test_dict = {
    "apple": 10,
    "banana": 20,
    "mango": 10,
    "orange": 30,
    "grapes": 10
}

print("Original Dictionary:", test_dict)


K = int(input("Enter the value to search for: "))
res = 0

for key in test_dict:
    if test_dict[key] == K:
        res += 1

print("Value:", K)
print("Frequency:", res)        