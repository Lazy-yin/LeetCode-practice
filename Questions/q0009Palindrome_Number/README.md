
# 009 Reverse Integer

檢查整數變數是否為回文，所以直覺想到的是將變數轉為字串，反轉後再比較，最後回傳結果。

### Example:

```python
若 x = 14541
反轉後為 14541，則要回傳 True

若 x = 1450
反轉後為 0541，則要回傳 False

```

## Solution

```python
def isPalindrome(x):
    if x >= 0:
        num = str(x)
        #將轉成字串的 x (num)，利用同時能在 list 或 str 上都能反轉的功能[::-1]
        #將 num 反轉後，比較兩者，或相同，則回傳 True，不同，則回傳 False
        re_num = num[::-1] 
        return True if num == re_num else False
    elif x > 2**31-1 or x<0:
        return False
```  

## Note

python 中有兩個簡單的反轉功能，一個為 [::-1]，另一個為 .reverse()
[::-1] 能使用在 list 或 str上，
但 .reverse() 只能使用在 list

#### 假設有以下參數 : 
```python
x = 14541
```
說明 : 
```python
若 x = 14541，轉換成字串後，反轉，會得到 re_num = 14541
再判斷 x = 14541 == re_num = 14541，因此回傳 True。
```
#### 假設有以下參數 : 
```python
若 x = 1450
```
說明 : 
```python
若 x = 1450，轉換為字串後，反轉，會得到 re_num = 0541
再判斷 x = 1450 != re_num = 0541，因此回傳 False
```

## Another solution
我不太確定直接使用 python 當中的 [::-1] 功能比較耗用記憶體，
還是 for 迴圈比較耗用記憶體，但總之也寫了一個簡單的 for 迴圈版本，
有空再來補上完全的 int 寫法吧...
```python
def isPalindrome(x):
    if x > 2**31-1 or x < 0:
        return False
    elif 0 <= x <10 :
        return True
    elif x >9 :
        num = str(x)
        for i in range(len(num)//2):
            if num[i] == num[len(num) - 1 - i]:
                continue
            elif num[i] != num[len(num) - 1 - i]:
                return False
        return True
```