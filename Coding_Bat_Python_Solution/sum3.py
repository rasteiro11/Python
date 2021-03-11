def sum3(nums):
    sum = 0
    for i in range(0, 3):
        sum = sum + nums[i]
    return sum


print(sum3([1, 2, 3]))