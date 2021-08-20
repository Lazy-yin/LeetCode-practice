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
## Solution II 
同樣是使用 stack solution ，但是著讓程式看起來更簡短
```python
    def isValid(self, s):
        save = []
        # s 的長度奇數直接回傳 False   
        if len(s)%2 == 1:
            return False
        if len(s) > 1:
            for ch in s : 
                #分成兩大類，頭跟尾，頭的話放入，尾的話取出
                if ch in "([{":
                    save.append(ch)
                    continue
                if ch in ")]}":
                    #遇到尾但清單是空的，所以直接回傳 False
                    if  not save:
                        return False
                    #遇到對應的尾，取出對應的頭
                    elif ch == ")" and save[-1] == "(":
                        save.pop()
                        continue
                    elif ch == "]" and save[-1] == "[":
                        save.pop()
                        continue
                    elif ch == "}" and save[-1] == "{":
                        save.pop()
                        continue
                    #通通都取不出來時請哭哭回傳 False
                    else:
                        return False
            #確認一下存放的清單在最後使否為空，是的話會回傳 True
            return not save
```

## Solution III
再試著讓程式變得更短

```python
def isValid(s):
    dic = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    save = []
    for i in s:
        #如果東西有在 dict中，就存入 i
        if i in dic:
            save.append(i)
        # not save : 出現左半邊，但 save 當中又沒有東西可取出時，一定為錯
        # dic[save.pop()] !=i : 去除掉 save 最後面的值，若對應 dict 後，
        # 與 i 不同，代表不成對，回傳錯誤
        elif not save or dic[save.pop()] !=i:
           return False 
    # 所有迴圈結束後 save 為空，表示括弧寫法正確       
    if not save:
        return True
```