def strStr(haystack, needle):
    count = 0
    if len(needle) == 0:
        return 0
    elif needle not in haystack:
        return -1
    elif needle in haystack:
        for i in range(len(haystack)):
            if needle == haystack[i:len(needle)+i]:
                return count
            elif needle != haystack[i:len(needle)+i]:
                count +=1