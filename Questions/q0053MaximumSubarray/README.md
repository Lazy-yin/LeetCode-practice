# 053 Maximum Subarray

計算 nums 串列中，尋找連續的串列元素中加總的最大值，並回傳其加總的最大值。

### Example:

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = 6
```

## Solution

```python
def maxSubArray(nums):
    temporary = nums[0]
    max = nums[0]
    for i in range(1,len(nums)):
        temporary += nums[i]
        #當串列中的元素大於暫存值時，暫存值被取代為元素值
        if nums[i] > temporary:
            temporary = nums[i]
            #當暫存值大於最大值時，更新最大值
            if max <= temporary:
                max = temporary
            elif max > temporary:
                pass
        #當暫存值大於串列中的元素時，暫存值不變
        elif nums[i] <= temporary:
            #當暫存值大於最大值時，更新最大值
            if max <= temporary:
                max = temporary
            elif max > temporary:
                pass            
    return max
```  

### 時間複雜度

方法中需要隨著 nums 的長度做 len(nums)-1 個步驟，因此為 O(n)。

## Note
假設有以下參數 :
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```
說明 :
```python
以下用  
t 代表 temporary
m 代表 max

        t = -2
        m = -2
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
       
i = 1 時，
nums = [-2,1,-3,4,-1,2,1,-5,4]
           t = 1，因為 (-2+1) < nums[1] = 1，所以被取代為 1
           m = 1，因為 -2 < t = 1，所以被取代為 1

i = 2 時，
nums = [-2,1,-3,4,-1,2,1,-5,4]
              t = -2，因為 (1-3) > nums[2] = -3，所以 t 不變
              m = 1，因為 1 > t = -2 ，所以 m 不變

i = 3 時
nums = [-2,1,-3,4,-1,2,1,-5,4]
                t = 4，因為 (-2+4) < nums[3] = 4，所以被取代為 4
                m = 4，因為 1 < t = 4 ，所以被取代為 4

i = 4 時
nums = [-2,1,-3,4,-1,2,1,-5,4]
                   t = 3，因為 (4-1) < nums[4] = -1，所以不變
                   m = 4，因為 4 < t = 3 ，所以不變

i = 4 時
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                          t = 3，因為 (4-1) < nums[4] = -1，所以不變
                          m = 4，因為 4 < t = 3 ，所以不變

i = 5 時
nums = [-2,1,-3,4,-1,2,1,-5,4]
                     t = 5，因為 (3+2) > nums[5] = 2，所以不變
                     m = 5，因為 4 < t = 5 ，所以被取代為 5

i = 6 時
nums = [-2,1,-3,4,-1,2,1,-5,4]
                       t = 6，因為 (5+1) > nums[6] = 1，所以不變
                       m = 6，因為 5 < t = 6 ，所以被取代為 6

i = 7 時
nums = [-2,1,-3,4,-1,2,1,-5,4]
                          t = 1，因為 (6-5) > nums[7] = -5，所以不變
                          m = 6，因為 6 > t = 1 ，所以不變

i = 8 時
nums = [-2,1,-3,4,-1,2,1,-5,4]
                            t = 5，因為 (1+4) > nums[8] = 4，所以不變
                            m = 6，因為 6 > t = 5 ，所以不變

最後回傳 m (max 的值)
```

