
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i,j in enumerate(nums):
        leave = target - nums[i]
        if leave in dict:
            ans = [i, dict[leave]]
            return ans
        else :
            dict[j] = i


nums = [2,7,11,15]
target = 9

list = twoSum(nums,target)

if nums[list[0]]+nums[list[1]] == target:
    print("true")
else:
    print("false")

