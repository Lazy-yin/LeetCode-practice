def lengthOfLastWord(s):
    seperate = s.split()
    lastword = seperate[len(seperate)-1]
    return(len(lastword))