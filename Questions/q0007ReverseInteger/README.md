
# 007 Reverse Integer

直接想到的暴力解就是把 int 轉成 str 後，由後往前一個一個加上去，最後回傳結果。

### Example:

```python
x = 120

經過轉換後應該要能回傳 21
```

## Solution

```python
    def reverse(self, x):
        if x==0:
            return 0
        if x > 0:
            num = str(x)
            ans = ""
            #將 x 轉為str後，利用其接近 list 的性質，讓字元由後往前加
            for i in range(len(num)):
                re_num = num[len(num) - i - 1]
                ans = ans + re_num
            #修正開頭為 0 時的狀況
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
        
```  

### 時間複雜度

上面的方法需要跑過 n 遍 ，所以為 O(N)。


## Note
假設有以下參數 :
```python
x = 120
```
說明 :
```
i = 0，re_num = num[ 3 - 0 - 1] = num[2] = 0
ans = 0

i = 1，re_num = num[ 3 - 1 - 1] = num[1] = 2
ans = 02

i = 2，re_num = num[ 3 - 2 - 1] = num[0] = 1
ans = 021

再經由去除開頭的 0，和判斷是否超過 int 的範圍後，回傳答案。

```

## Another solution
```python
def reverse(self, x):    
    if x > 0:
        a = str(x)
        a = a[::-1]
        return int(a) if int(a) <= 2 **31-1 else 0
    else:
        x = x*(-1)
        a = str(x)
        a = a[::-1]
        return int(a)*(-1) if int(a) <= 2 **31-1 else 0
```
## Note
```python
在 python 中有更加簡單的方法讓整個 list 反轉，就就是使用 [::-1]。
```