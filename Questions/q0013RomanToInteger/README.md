# 012 Romanto Integer

最先想到的暴力解就是字串由後往前辨識，如果遇到相同或更大的值就會相加，如果是比較小的就會是相減。

### Example:

```python
s = XIV
ans = 14 
```

## Solution

```python
def romanToInt(s):
    #建立出羅馬數字中字母對應的數值清單。
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    table = "I"
    #當字串長度為 1 時，可以直接
    if len(s) == 1:
        return value[s]
    elif 1 < len(s) < 16:
        for i in range(len(s)):
            #字串由後往前看，如果對照出來的 int 相同或比較大，則存起來(table)，並且加上去
            if value[s[len(s)-i-1]] >= value[table]:  
                table = s[len(s)-i-1]
                ans = ans + value[table]
            #如果對照出來的 int 比較小，
            elif value[s[len(s)-i-1]] < value[table]:
                ans = ans - value[s[len(s)-i-1]]
        return ans 
```  
### 時間複雜度
此方法需要隨著 s 的長度，跑過 n 個步驟 ，所以為 O(n)。

## Note
假設有以下參數 : 
```python
s = XIV
```
說明 : 
```python
ans = 0
table = "I"
len(s) = 3

當 i = 0 時
value[s[3-0-1]] = value[s[2]] = value["V"] = 5 >= value[table] = value["I"] = 1
此時，table 會被取代成為 s[len(s)-i-1] = "V"
而 ans = ans + value[table] = 0 + value["V"] = 0 + 5 = 5

當 i = 1 時
value[s[3-1-1]] = value[s[1]] = value["I"] = 1 < value[table] = value["V"] = 5
此時，table 不變，
而 ans = ans - value[s[len(s)-i-1]] = 5 - value["I"] = 5 - 1 = 4

當 i = 2 時
value[s[3-2-1]] = value[s[0]] = value["X"] = 10 >= value[table] = value["V"] = 5
此時，table 會被取代成為 s[len(s)-i-1] = "X"
而 ans = ans + value[table] = 0 + value["X"] = 4 + 10 = 14

最後回傳 14

```
