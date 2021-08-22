def searchInsert(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i] < target:
            count +=1
        elif nums[i] >= target:
            return count
    return count