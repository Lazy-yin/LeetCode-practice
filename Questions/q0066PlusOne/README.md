# 066 Plus One

給一個串列作為向量，當向量值加一時，回傳加一後的向量串列

### Example:

```python
digits = [1,0,9,9,9]
ans = [1,1,0,0,0]
```

## Solution

```python
def plusOne(digits):
    number = ""
    answer = []
    if len(digits) < 1 or len(digits) >100:
        return answer
    #將串列轉回字串    
    for i in range(len(digits)):
        number += str(digits[i])
    #將字串轉為數字後 +1
    plusone = int(number) + 1
    #將加一後的數字轉回串列
    for j in str(plusone):
        answer.append(int(j))
    return answer
```  

## Note
假設有以下參數 :
```python
digits = [1,0,9,9,9]
```
說明 :
```python
digits = [1,0,9,9,9]

由串列轉為字串
number = 10999

加一
plusone = 11000

由數字轉為串列
answer = [1,1,0,0,0]

回傳 answer
```

## Solution
前一方法是用串列轉文字轉數字在轉串列，此方法回到十進位來解題。
```python
def plusOne(digits):
    #判斷串列是否長度為 1 ，為 9 則直接回傳答案 [1,0]
    if len(digits) == 1 and digits[0] == 9:
        return [1,0]
    #判斷串列是否長度為 1 ，不為 9 則 +1 後回傳答案     
    elif  len(digits) == 1 and 0 < digits[0] < 9:
        digits[0] = digits[0]+1
        return digits
    #判斷最後元素是否為 9 ，否的話， +1 回傳答案
    elif 0 <= digits[-1] < 9:
        digits[-1] = digits[-1] + 1
        return digits
    #若為 9 ，則該元素變為 0，前一位數 +1
    elif digits[-1] == 9:
        digits[-1] = 0
        digits[-2] +=1
        for i in range(1,len(digits)-1):
            #由於經過 +1，若不為 10 則可直接回傳答案
            if 1 <= digits[len(digits)-1-i] <= 9:
                return digits
            #若為 10 ，則該元素變為 0，前一位數 +1
            elif digits[len(digits)-1-i] == 10:
                digits[len(digits)-1-i] = 0
                digits[len(digits)-2-i] = digits[len(digits)-2-i] +1
        #若首個元素為 10 ，則該元素變為 0，串列最前面補上一元素 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits
```

