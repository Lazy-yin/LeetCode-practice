def isValid(s):
    dic = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    save = []
    for i in s:
        if i in dic:
            save.append(i)
        elif not save or dic[save.pop()] !=i:
           return False 
    if not save:
        return True
