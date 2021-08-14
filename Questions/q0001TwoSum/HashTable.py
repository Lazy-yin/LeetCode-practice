
def twoSum(nums, target):
    dict = {}
    for i,j in enumerate(nums):
        leave = target - nums[i]
        if leave in dict:
            ans = [i, dict[leave]]
            return ans
        else :
            dict[j] = i

