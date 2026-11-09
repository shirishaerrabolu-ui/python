class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

nums = (10, 20, 30, 40, 50, 60, 70)
target = int(input("Enter target sum: "))

p = pair_elements()
result = p.twoSum(nums, target)

print("Positions:", result)

