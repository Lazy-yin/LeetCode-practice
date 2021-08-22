# 027 Remove Element

在一個沒有排序過的串列中，與給其一個指定變數，將串列重新整理過，使其最後回傳去除掉指定變數後的串列。

### Example:
```
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
ans = [0, 1, 3, 0, 4, _, _, _]
```

## Solution

```python
def removeElement(nums,val):
    count = 0
    for i in range(len(nums)):
        #將不同於指定變數的元素移到指定位置
        if nums[i] != val:
            nums[count] = nums[i]
            count +=1
    return count
```  

### 時間複雜度

上面的方法需要跑過 n 遍 ，所以為 O(n)。

## Note
假設有以下參數 :
```python
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
```
說明 :
```python

  i     nums[i]    count   nums
  0        0         1     [0, 1, 2, 2, 3, 0, 4, 2]
  1        1         2     [0, 1, 2, 2, 3, 0, 4, 2]
  2        2         2     [0, 1, 2, 2, 3, 0, 4, 2]
  3        2         2     [0, 1, 2, 2, 3, 0, 4, 2]
  4        3         3     [0, 1, 3, 2, 3, 0, 4, 2]
  5        0         4     [0, 1, 3, 0, 3, 0, 4, 2]
  6        4         5     [0, 1, 3, 0, 4, 0, 4, 2]
  7        2         5     [0, 1, 3, 0, 4, 0, 4, 2]

最後統計出與指定變數不同的有5個
回傳 5 (count 的值)
```

