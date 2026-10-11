nums = [1, 2, 3]
print(nums)

biggest_item = max(nums)
smallest_item = min(nums)

print("the biggest item:", biggest_item)
print("the smallest item:", smallest_item)

print("our algorithm:")

biggest = nums[0]
for i in range(len(nums)):
    if nums[i] > biggest:
        biggest = nums[i]
print("the biggest item:", biggest)