def reverse3(nums):
    rotate = []
    for i in range(len(nums)-1, -1, -1):
        rotate.append(nums[i])

    return rotate

print(reverse3([11, 12, 13, 14]))
