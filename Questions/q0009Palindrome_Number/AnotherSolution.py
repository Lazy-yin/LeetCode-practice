def isPalindrome(x):
    if x > 2**31-1 or x < 0:
        return False
    elif 0 <= x <10 :
        return True
    elif x >9 :
        num = str(x)
        for i in range(len(num)//2):
            if num[i] == num[len(num) - 1 - i]:
                continue
            elif num[i] != num[len(num) - 1 - i]:
                return False
        return True