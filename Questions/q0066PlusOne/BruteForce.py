def plusOne(digits):
    number = ""
    answer = []
    if len(digits) < 1 or len(digits) >100:
        return answer
    for i in range(len(digits)):
        number += str(digits[i])
    plusone = int(number) + 1
    for j in str(plusone):
        answer.append(int(j))
    return answer