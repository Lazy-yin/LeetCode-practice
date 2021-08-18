# 014 Longest Common Prefix

題目題幹是要找到最長的相同的前綴詞，然而題目敘述中也有講到 input 的清單長度在 0~200之間，
而清單中的元素字長在 1~200之間，如果直接從第一個開始比對，萬一字長直接200，會比對到瘋掉...

#### 因此我採用的方法是
1. 先從清單中找到最短的元素
2. 讓最短的元素中由第一個字母依序往後比 
3. 若有相同者存入另一個清單(save)
4. 從 save 清單中找到最短的那個就是答案

### Example:

```python
strs = ["flower","flow","flight"]
answer = "fl"
```

## Solution

```python
def longestCommonPrefix(strs):

    x=0
    save = ""
    result = []
    #先將清單中的元素一一比，找出最短的那個，遇到有更短的就存進 x 中。
    for y in range(len(strs)):
        if len(strs[x]) > len(strs[y]):
            x = y
    
    #將清單中的元素枚舉以便後面比較
    for num,lists in enumerate(strs):
        #將字母由第一個開始依序往後比較，若相同則存入save，並進到下一個字母，若無則直接離開迴圈
        for i in range(len(strs[x])):  
            if strs[x][i] == strs[num][i]:
                save = save + strs[x][i]
            elif  strs[x][i] != strs[num][i]:
                break
        #將最後得到結果存入 result 這個清單中
        result.append(save)
        save = ""
    ans = 0

    #將 result 清單中找出最短的那個，即是答案
    for z in range(len(result)):
        if len(result[ans]) > len(result[z]):
            ans = z
    return result[ans]

```  

### 時間複雜度

超級複雜，因為跑過了各式各樣的迴圈
1. 先從清單中找到最短的元素，因為跑過 N 個元素，所以是 O(n)
2. 讓最短的元素中由第一個字母依序往後比 ，先將第一個字母與清單中元素比較，再比較第二個字母，由此可知為 N**2，所以是 O(N^2)
3. 若有相同者存入另一個清單(save)
4. 從 save 清單中找到最短的那個就是答案，因為跑過 N 個元素，所以是 O(n)


## Note
假設有以下參數 :
```python
strs = ["flower","flow","flight"]
```
說明 :
```python
1. 先從清單中找到最短的元素

flow 是清單中最短的元素，因此可得到 len(strs[1]) = 4，
此時 x = 1

2. 讓最短的元素中由第一個字母依序往後比 
3. 若有相同者存入另一個清單(save)

先將 strs 枚舉，再比較最短元素中的第一個字母，若有則放入 save 保存，無則跳出迴圈
num   lists        strs[x][0] = "f"       save +=strs[x][0]
 0   "flower"            有                       f
 1   "flow"              有                       f
 2   "flight"            有                       f


  strs 的枚舉，再比較最短元素中的第二個字母，若有則放入 save 保存，無則跳出迴圈
num   lists        strs[x][1] = "l"       save +=strs[x][1]
 0   "flower"            有                       fl
 1   "flow"              有                       fl
 2   "flight"            有                       fl


  strs 的枚舉，再比較最短元素中的第三個字母，若有則放入 save 保存，無則跳出迴圈
num   lists        strs[x][2] = "o"       save +=strs[x][2]
 0   "flower"            有                       flo
 1   "flow"              有                       flo
 2   "flight"            無                    跳出迴圈

  strs 的枚舉，再比較最短元素中的第四個字母，若有則放入 save 保存，無則跳出迴圈
num   lists        strs[x][3] = "o"       save +=strs[x][3]
 0   "flower"            有                       flow
 1   "flow"              有                       flow

4. 從 save 清單中找到最短的那個就是答案
最後 save = ["flow", "flow", "fl"]
而最短的 "fl" 即是解答 
所以回傳 "fl"


```

