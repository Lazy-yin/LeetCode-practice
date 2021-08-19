from Questions.q0020ValidParentheses.StackSolution import isValid

# s = "()[]{}"
# ans = True

s = "([)]"
ans = False

output = int(isValid(s))

if ans == output :
    print("right answer")
else:
    print("false")