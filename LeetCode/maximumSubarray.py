nums = [-2,1,-3,4,-1,2,1,-5,4]
start = nums[0]
next = nums[0]
for i in range(1, len(nums)):
    start = max(start + nums[i], nums[i])
    next = max(start, next)
    print(i, nums[i], start, next)

