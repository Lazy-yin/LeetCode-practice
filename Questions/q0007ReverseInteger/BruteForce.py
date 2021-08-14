def reverse(x):
    if x==0:
        return 0
    if x > 0:
        num = str(x)
        ans = ""
        for i in range(len(num)):
            re_num = num[len(num) - i - 1]
            ans = ans + re_num
        ans = ans.lstrip("0")
        return ans if int(ans) < 2**31 else 0
    if x < 0:
        num = str(x*(-1))
        ans = ""
        for i in range(len(num)):
            re_num = num[len(num) - i - 1]
            ans = ans + re_num
        ans = "-" + ans.lstrip("0")
        return ans if int(ans) > -2**31 else 0