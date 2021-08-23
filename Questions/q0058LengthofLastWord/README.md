# 058 Length of Last Word

在字串中，找到最後一個字，並且回傳它的字長

### Example:

```python
s = "   fly me   to   the moon  "
ans = 4
```

## Solution

```python
def lengthOfLastWord(s):
    #去除中間的空白，並且存進串列中
    seperate = s.split()
    lastword = seperate[len(seperate)-1]
    return(len(lastword))
```  

## Note
假設有以下參數 :
```python
s = "   fly me   to   the moon  "
```
說明 :
```python

s = "   fly me   to   the moon  "

經由 python 的 split 功能，將字串中的空白去除，
並且把切割後的字串存進串列中

seperate = ['fly', 'me', 'to', 'the', 'moon']

回傳串列中最後一個字串的長度
```

