def maxSubArray(nums):
    temporary = nums[0]
    max = nums[0]
    for i in range(1,len(nums)):
        temporary += nums[i]
        if nums[i] > temporary:
            temporary = nums[i]
            if max <= temporary:
                max = temporary
            elif max > temporary:
                pass
        elif nums[i] <= temporary:
            if max <= temporary:
                max = temporary
            elif max > temporary:
                pass
            
    return max