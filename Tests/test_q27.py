from Questions.q0027RemoveElement.BruteForce import removeElement

nums =[0,1,2,2,3,0,4,2]
val = 2
ans = [0,1,3,0,4]
output = removeElement(nums, val)
for i in range(output):
    if ans[i] in nums:
        nums.remove(ans[i])
    elif ans[i] not in nums:
        print("wrong answer")
        break
print("right answer")