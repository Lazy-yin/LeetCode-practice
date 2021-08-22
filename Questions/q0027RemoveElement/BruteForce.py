def removeElement(nums,val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count +=1
    return count

nums =[0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))            