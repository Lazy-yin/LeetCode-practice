def addBinary(a, b):
    total = str(int(a) + int(b))
    totalist = []
    answer = ""
    if 0 <= int(total) <2 :
        return total
    elif int(total) == 2:
        return str(10)
    elif int(total) == 3:
        return str(11)
    for j in range(len(total)):
        totalist.append(int(total[j]))
    answerlist = []
    for i in range(len(totalist)-1):
        if 0 <= totalist[len(totalist)-1-i] <=1:
            answerlist.insert(0,totalist[len(totalist)-1-i]) 
        elif totalist[len(totalist)-1-i] == 2:
            answerlist.insert(0,0)
            totalist[len(totalist)-i-1] = 0
            totalist[len(totalist)-i-2] +=1
        elif totalist[len(total)-1-i] == 3:
            answerlist.insert(0,1)
            totalist[len(totalist)-i-1] = 1
            totalist[len(totalist)-i-2] +=1
    if totalist[0] ==1:
        answerlist.insert(0,1)
    elif totalist[0] ==2:
        answerlist.insert(0,0)
        answerlist.insert(0,1)
    elif totalist[0] ==3:
        answerlist.insert(0,1)
        answerlist.insert(0,1)
    for m in range(len(answerlist)):
        answer += str(answerlist[m])
    return answer