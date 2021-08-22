# 028 Implement strStr

檢查 haystack 中是否有 needle 字串在其中，若有，在字串中的哪個位置。

### Example:

```python
haystack = "aaaeeerrr"
needle = "ee"
ans = 3
```

## Solution

```python
def strStr(haystack, needle):
    count = 0
    if len(needle) == 0:
        return 0
    elif needle not in haystack:
        return -1
    elif needle in haystack:
        for i in range(len(haystack)):
            if needle == haystack[i:len(needle)+i]:
                return count
            elif needle != haystack[i:len(needle)+i]:
                count +=1
```  

### 時間複雜度

方法中需要隨著 haystack 的長度做 len(haystack) 個步驟，因此為 O(n)。

## Note
假設有以下參數 :
```python
haystack = "aaaeeerrr"
needle = "ee"
```
說明 :
```python
  i      count    needle    haystack[i:len(needle)+i]
  0        0        ee       aa      haystack[0:2]
  1        1        ee       aa      haystack[1:3]
  2        2        ee       ae      haystack[2:4]
  3        3        ee  ==   ee      haystack[3:5]    return count



回傳 count
```

