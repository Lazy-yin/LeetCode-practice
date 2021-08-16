from Questions.q0009Palindrome_Number.BruteForce import isPalindrome
# from Questions.q0009Palindrome_Number.AnotherSolution import isPalindrome

x = 14541
# x = 1450
# x = -110000000000000000011
# x = 123456789098

output = True
ans = int(isPalindrome(x))
if ans == output and ans == True:
    print("is Palindrome")
else:
    print("not Palindrome")