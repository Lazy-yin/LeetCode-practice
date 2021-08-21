def removeDuplicates(nums):
    j = 0
    n = len(nums)
    if n == 0 :
        return j
    elif n == 1:
        return j+1
    elif n > 1:
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                j += 1
                nums[j] = nums[i+1]
        return j+1

