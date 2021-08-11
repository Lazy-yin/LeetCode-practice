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