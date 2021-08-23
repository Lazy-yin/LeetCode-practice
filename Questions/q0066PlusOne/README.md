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

