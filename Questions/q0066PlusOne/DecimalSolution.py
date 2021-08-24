def plusOne(digits):
    if len(digits) == 1 and digits[0] == 9:
        return [1,0]
    elif  len(digits) == 1 and 0 < digits[0] < 9:
        digits[0] = digits[0]+1
        return digits
    elif 0 <= digits[-1] < 9:
        digits[-1] = digits[-1] + 1
        return digits
    elif digits[-1] == 9:
        digits[-1] = 0
        digits[-2] +=1
        for i in range(1,len(digits)-1):
            if 1 <= digits[len(digits)-1-i] <= 9:
                return digits
            elif digits[len(digits)-1-i] == 10:
                digits[len(digits)-1-i] = 0
                digits[len(digits)-2-i] = digits[len(digits)-2-i] +1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits