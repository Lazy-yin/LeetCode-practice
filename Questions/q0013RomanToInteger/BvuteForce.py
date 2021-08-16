def romanToInt(s):
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    table = "I"
    if len(s) == 1:
        return value[s]
    elif 1 < len(s) < 16:
        for i in range(len(s)):
            if value[s[len(s)-i-1]] >= value[table]:  
                table = s[len(s)-i-1]
                ans = ans + value[table]
            elif value[s[len(s)-i-1]] < value[table]:
                ans = ans - value[s[len(s)-i-1]]
        return ans    
