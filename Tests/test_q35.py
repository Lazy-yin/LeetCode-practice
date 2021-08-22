from Questions.q0035SearchInsertPosition.BruteForce import searchInsert

nums = [1,3,5,6]
target = 5
ans = 2

output = searchInsert(nums,target)

if ans == output:
    print("Right")
else:
    print("Wrong")
