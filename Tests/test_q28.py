from Questions.q0028ImplementstrStr.BruteForce import strStr

# haystack = "eeerrr"
# needle = "e"
# ans = 0

haystack = "aaaeeerrr"
needle = "ee"
ans = 3

output = strStr(haystack, needle)
if output == ans:
    print("right answer")
else:
    print("wrong answer")