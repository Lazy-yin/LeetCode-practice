def isValid(s):
    dic = {"(":"A", 
            ")":"A", 
            "[":"B", 
            "]":"B", 
            "{":"C", 
            "}":"C"
            }
    stack_list = []
    if len(s)%2 == 1:
        return False
    if len(s)%2 == 0:
        if len(s) == 0:
            return True
        elif s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        elif s[-1] == "(" or s[-1] == "{" or s[-1] == "[":
            return False
        for i in range(len(s)):
            if s[i] == "(":
                stack_list.append(dic["("])
            if s[i] == "[":
                stack_list.append(dic["["])
            if s[i] == "{":
                stack_list.append(dic["{"])
            if s[i] == ")":
                if len(stack_list) > 0 and stack_list[-1] == dic[")"]:
                    stack_list = stack_list[:-1]
                else:
                    return False
            if s[i] == "]":
                if len(stack_list) > 0 and stack_list[-1] == dic["]"]:
                    stack_list = stack_list[:-1]
                else:
                    return False
            if s[i] == "}":
                if len(stack_list) > 0 and stack_list[-1] == dic["}"]:
                    stack_list = stack_list[:-1]
                else:
                    return False
        if len(stack_list)==0:
            return True