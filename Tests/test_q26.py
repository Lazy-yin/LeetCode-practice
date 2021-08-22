from Questions.q0026RemoveDuplicatesfromSortedArray.BruteForce import removeDuplicates

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
ans = [0, 1, 2, 3, 4]

# output =removeDuplicates(nums)
out = removeDuplicates(nums)
for i in range(out):
    if ans[i] in nums:
        pass
    elif ans[i] not in nums:
        print("wrong answer")
        break
print("right answer")