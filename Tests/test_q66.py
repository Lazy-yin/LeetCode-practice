from Questions.q0066PlusOne.BruteForce import plusOne

digits = [1,0,9,9,9]
ans = [1,1,0,0,0]

output = plusOne(digits)

if ans == output:
    print("right")
else:
    print(output)
    print("wrong")