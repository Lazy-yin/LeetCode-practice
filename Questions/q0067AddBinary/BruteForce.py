def addBinary(a, b):
    if a[0] == 0 or b[0] == 0:
        return False
    if len(a) > 10**4 or len(b) > 10**4:
        return False
    numbera = 0
    numberb = 0
    for i in range(len(a)):
        numbera += (2**i * int(a[len(a)-1-i]))
    for j in range(len(b)):
        numberb += (2**j * int(b[len(b)-1-j]))
    total = numbera + numberb
    longlen = 0
    answer =""
    if len(a) >= len (b):
        longlen = len(a)
    elif len(b) > len(a):
        longlen = len(b)
    if total >= 2**longlen:
        for x in range(longlen+1):
            if total >= 2**(longlen - x):
                total -= 2**(longlen - x)
                answer += str(1)
            elif total < 2**(longlen - x):
                answer += str(0)
        return answer 
    elif total < 2**longlen:
        for x in range(longlen):
            if total >= 2**(longlen - 1 - x):
                total -= 2**(longlen - 1 - x)
                answer += str(1)
            elif total < 2**(longlen - 1 - x):
                answer += str(0)
        return answer 