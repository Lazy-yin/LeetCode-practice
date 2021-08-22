# 035 Search Insert Position

nums 是一個經排序的串列，將 target 插入串列中，回傳其所在位置。

### Example:

```python
nums = [1,3,5,6]
target = 5
ans = 2
```

## Solution

```python
def searchInsert(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i] < target:
            count +=1
        elif nums[i] >= target:
            return count
    return count
```  

### 時間複雜度

方法中需要隨著 nums 的長度做 len(nums) 個步驟，因此為 O(n)。

## Note
假設有以下參數 :
```python
nums = [1,3,5,6]
target = 5
```
說明 :
```python
  i      nums[i]    target   count
  0        1     <    5        1
  1        3     <    5        2
  2        5     >=   5      return count  
  3        6          5


回傳 count
```

