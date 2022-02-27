nums = [1,2,3,4]
# nums = [-1, 1, 0, -3, 3]
res = [1] * (len(nums))
prefix = 1
for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
    print(i, res[i], nums[i], prefix)
print (res)
postfix = 1
for i in range(len(nums) -1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
    print(i, res[i], nums[i], postfix)

print (res)


