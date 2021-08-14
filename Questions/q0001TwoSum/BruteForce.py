def twoSum(self, nums, target):
    
    ans = []
    for i in range(len(nums)-1):
        leave = target - nums[i]
        for j in range(1,len(nums)):
            if nums[j] == leave:
                return [i,j]    
                