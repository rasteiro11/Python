def sum2(nums):
    sum = 0
    for i in range(0, 2):
        sum += nums[i]
    return sum


print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))

