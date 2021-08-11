from Questions.q0001TwoSum.HashTable import twoSum

nums = [2,7,11,15]
target = 9

list = twoSum(nums,target)

if nums[list[0]]+nums[list[1]] == target:
    print("true")
else:
    print("false")