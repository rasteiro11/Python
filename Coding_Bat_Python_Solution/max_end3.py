def max_end3(nums):
    a = []
    if nums[0] > nums[len(nums) - 1]:
        for i in range(0, len(nums)):
            a.append(nums[0])
    if nums[len(nums) - 1] > nums[0]:
        for i in range(0, len(nums)):
            a.append(nums[len(nums) - 1])
    if nums[len(nums) - 1] == nums[0]:
        for i in range(0, len(nums)):
            a.append(nums[0])
    return a



print(max_end3([1, 2, 3]))
print(max_end3([2, 11, 3]))
print(max_end3([11, 5, 9]))






