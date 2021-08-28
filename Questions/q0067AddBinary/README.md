# 067 Add Binary

給予兩個變數(str type) ，用於表示二進位法，題目要求將兩者相加後同樣以二進位型式回傳答案。

### Example:

```python
a = str(101100)
b = str(1111)
ans = str(111011)
```

## Solution

```python
def addBinary(a, b):
    #二進位法開頭為 0 者為錯
    if a[0] == 0 or b[0] == 0:
        return False
    #題目規定的 a 與 b 兩者的長度範圍
    if len(a) > 10**4 or len(b) > 10**4:
        return False
    numbera = 0
    numberb = 0
    #將 a 與 b 轉成十進位制
    for i in range(len(a)):
        numbera += (2**i * int(a[len(a)-1-i]))
    for j in range(len(b)):
        numberb += (2**j * int(b[len(b)-1-j]))
    total = numbera + numberb
    longlen = 0
    answer =""
    #判斷 a 與 b 何者長度較長(通常也代表可能值較大)
    if len(a) >= len (b):
        longlen = len(a)
    elif len(b) > len(a):
        longlen = len(b)
    #如果加總後數值進位，則將範圍 +1
    if total >= 2**longlen:
        #藉由逐漸扣除加總後的值，將其轉為二進位
        for x in range(longlen+1):
            if total >= 2**(longlen - x):
                total -= 2**(longlen - x)
                answer += str(1)
            elif total < 2**(longlen - x):
                answer += str(0)
        return answer 
    #若無加總後的數值進位，則將範圍保持在與 a 或 b 相同即可 
    elif total < 2**longlen:
        for x in range(longlen):
            if total >= 2**(longlen - 1 - x):
                total -= 2**(longlen - 1 - x)
                answer += str(1)
            elif total < 2**(longlen - 1 - x):
                answer += str(0)
        return answer 
```  
### 時間複雜度

方法中需要先將 a 與 b 由二進位轉為十進位，需要隨著字串長度做 n 個步驟，因此為 O(n)。
再將十進位轉為二進位，亦隨著字串長度做 n 個步驟，因此為 O(n)

## Note
假設有以下參數 :
```python
a = str(101100)
b = str(1111)
```
說明 :
```python
a = str(101100)
0+0+4+8+0+32 = 
b = str(1111)

將 a, b 轉為十進位
numbera = 32+0+8+4+0+0 = 44
numberb = 8+4+2+1 = 15

加總後
total = numbera + numberb = 59

比較 a 與 b 何者較大 
len(a) = 6
len(b) = 4
所以 longlen = 6

而 2**6 = 64 > total，所以未進位

total = 59
將十進位轉為二進位
在範圍 0~5間
2**5 = 32
total = 59 - 32 = 27
answer = 1

2**4 = 16
total = 27 - 16 = 11
answer = 11

2**3 = 8
total = 11 - 8 = 3
answer = 111

2**2 = 4
total = 3 < 4
answer = 1110

2**1 = 2
total = 3 - 2 = 1
answer = 11101

2**0 = 1
Total = 1-1 = 0
answer = 111011
```

#### 但將 a 與 b 轉為十進位法再加總後再轉回二進位法實在是太耗費記憶體空間了，因此又寫了一個單純二進位計算的方法。

## Solution
```python
def addBinary(a, b):
    #總之先加起來
    total = str(int(a) + int(b))
    totalist = []
    answer = ""
    if 0 <= int(total) <2 :
        return total
    elif int(total) == 2:
        return str(10)
    elif int(total) == 3:
        return str(11)
    #先將 total 轉為串列
    for j in range(len(total)):
        totalist.append(int(total[j]))
    answerlist = []
    #逢二進一，由後往前依序漸進
    for i in range(len(totalist)-1):
        if 0 <= totalist[len(totalist)-1-i] <=1:
            answerlist.insert(0,totalist[len(totalist)-1-i]) 
        elif totalist[len(totalist)-1-i] == 2:
            answerlist.insert(0,0)
            totalist[len(totalist)-i-1] = 0
            totalist[len(totalist)-i-2] +=1
        elif totalist[len(total)-1-i] == 3:
            answerlist.insert(0,1)
            totalist[len(totalist)-i-1] = 1
            totalist[len(totalist)-i-2] +=1
    #判斷最前面的數值，若為 2 或 3，則須再進位
    if totalist[0] ==1:
        answerlist.insert(0,1)
    elif totalist[0] ==2:
        answerlist.insert(0,0)
        answerlist.insert(0,1)
    elif totalist[0] ==3:
        answerlist.insert(0,1)
        answerlist.insert(0,1)
    for m in range(len(answerlist)):
        answer += str(answerlist[m])
    return answer
```

## 最後的最後
python 之所以好用就是因為有很多已經寫好的工具可以用，包含了二進位法，而使用工具時也只要短短幾行就可以解決。
## Solution
```python
def addBinary(a, b):
    sum=bin(int(a,2)+int(b,2))
    return (sum[2:])
```