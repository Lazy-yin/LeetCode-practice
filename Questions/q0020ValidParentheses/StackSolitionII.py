def isValid(s):
    save = []   
    if len(s)%2 == 1:
        return False
    if len(s) > 1:
        for ch in s : 
            if ch in "([{":
                save.append(ch)
                continue
            if ch in ")]}":
                if  not save:
                    return False
                elif ch == ")" and save[-1] == "(":
                    save.pop()
                    continue
                elif ch == "]" and save[-1] == "[":
                    save.pop()
                    continue
                elif ch == "}" and save[-1] == "{":
                    save.pop()
                    continue
                else:
                    return False
        return not save