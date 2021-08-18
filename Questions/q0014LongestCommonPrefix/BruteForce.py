def longestCommonPrefix(strs):
    x=0
    save = ""
    result = []
    for y in range(len(strs)):
        if len(strs[x]) > len(strs[y]):
            x = y
    for num,lists in enumerate(strs):
        for i in range(len(strs[x])):  
            if strs[x][i] == strs[num][i]:
                save = save + strs[x][i]
            elif  strs[x][i] != strs[num][i]:
                break
        result.append(save)
        save = ""
    ans = 0    
    for z in range(len(result)):
        if len(result[ans]) > len(result[z]):
            ans = z
    return result[ans]