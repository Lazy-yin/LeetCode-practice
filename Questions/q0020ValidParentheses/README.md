# 020 Valid Parentheses
檢查不論是在程式、數學計算中都很重要的括弧， input 中的字串是否括弧寫法正確
### Example:

```python
s = "()[]{}"
Output : true

s = "([)]"
Output : false
```

## Solution

```python
def isValid(s):
    #先將各種括弧與其應對的符號先以 dictionary 形式儲存，以便後面對應使用
    dic = {"(":"A", 
            ")":"A", 
            "[":"B", 
            "]":"B", 
            "{":"C", 
            "}":"C"
            }
    #用於執行 stack solution 時，暫時存放的一維陣列
    stack_list = []
    #由於括弧都是成對出現，數量為奇數時必定為錯誤
    if len(s)%2 == 1:
        return False
    if len(s)%2 == 0:
        if len(s) == 0:
            return True
        #由於括弧有一定的頭尾順序，若出現以下兩種結果，必定為錯
        elif s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        elif s[-1] == "(" or s[-1] == "{" or s[-1] == "[":
            return False
        for i in range(len(s)):
            #開始 stack solution 
            #出現則存入
            if s[i] == "(":
                stack_list.append(dic["("])
            if s[i] == "[":
                stack_list.append(dic["["])
            if s[i] == "{":
                stack_list.append(dic["{"])
            #成對的半邊出現則取出，若無法取出則回傳 False
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
        #進行完對字串做的迴圈堆疊後，若暫時存放的一維陣列為 0，可得知 input 的字串為正確的括弧寫法 
        if len(stack_list)==0:
            return True
```  

### 時間複雜度

上面的方法需要跑過 n 遍 ，所以為 O(N)。


## Note
### 正確的情況，假設有以下參數 :
```python
s = "()[]{}"
Output : true
```
說明 :
```python
i = 0 時，s[0] = "("，因此將 A 存入 stack_list 中，
此時  stack_list = ["A"]

i = 1 時，s[1] = ")"，因此將 A 從 stack_list 的最外側移除，
此時  stack_list = []

i = 2 時，s[2] = "["，因此將 B 存入 stack_list 中，
此時  stack_list = ["B"]

i = 3 時，s[3] = "]"，因此將 B 從 stack_list 的最外側移除，
此時  stack_list = []

i = 4 時，s[4] = "("，因此將 C 存入 stack_list 中，
此時  stack_list = ["C"]

i = 5 時，s[5] = ")"，因此將 C 從 stack_list 的最外側移除，
此時  stack_list = []

結束迴圈後檢查 len(stack_list) = 0，回傳 True
```
## 錯誤的情況，假設有以下參數 :
```python

s = "([)]"
Output : false
```
說明 :
```python
i = 0 時，s[0] = "("，因此將 A 存入 stack_list 中，
此時  stack_list = ["A"]

i = 1 時，s[1] = "["，因此將 B 存入 stack_list 中，
此時  stack_list = ["A","B"]

i = 2 時，s[3] = ")"，此時須將 A 從最外側移除，
但 stack_list = ["A","B"] ，最外側並不是 A 因此回傳 False

```
### 對不起，我就是想 murmur 一下 QQ

```python
起初看到這題，只想著先把括弧的規則總結一下
1. 如果頭尾有對應的可以先扣除 
2. 括弧最內側的是鄰近的，所以一路扣，可以扣到剩很少，
   最後啥都不剩就回傳 True
3. 如果經過上面兩個步驟都沒有變少，就代表不是正確的括弧寫法，
   最後回傳 False
-------------------------------------------
朋友才看一眼就知道我的思考完全出錯!!!
但還是人很好的教我 stack solution，
演算法跟資料處理好重要QQQQQ 
```
