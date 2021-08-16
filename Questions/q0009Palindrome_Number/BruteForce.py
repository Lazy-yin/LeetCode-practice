def isPalindrome(x):
    if x >= 0:
        num = str(x)
        re_num = num[::-1] 
        return True if num == re_num else False
    elif x > 2**31-1 or x<0:
        return False