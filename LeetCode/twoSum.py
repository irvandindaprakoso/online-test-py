def twoSum(nums, target):
    m = {}
    r = []
    for i, n in enumerate(nums):
        if target-n in m:
            r=[m[target-n], i]
        m[n]=i
    return r

print(twoSum([2,7,11,15],9))
