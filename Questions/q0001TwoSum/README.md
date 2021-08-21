
# 001 TwoSum

最先想到的是暴力解，先把一個數字固定下來，
讓目標值減掉固定值後得到差值，尋找有沒有符合差值的，
若沒有便將固定的數字移到下一個。

### Example:

```python
nums = [1, 10, 100, 1000]
target = 1010

Because nums[1] + nums = [3] = 10 + 1000 = 1010
return [0,1]

```

## Solution

```python
def twoSum(nums, target):

    for i in range(len(nums)-1):
        leave = target - nums[i]
        #先固定其中一個數值，讓目標數扣掉數值後留下一個值
        for j in range(1,len(nums)):
            if nums[j] == leave:
            #將值依序往後比對，相同，則回傳    
                return [i,j] 
```  

### 時間複雜度

上面的方法需要跑過 n(n+1)/2 ，所以為 O(n^2)。


## Solution

```python
def twoSum(nums, target):
    # 先創建一個dictionary 放置迭代後的資料
    dict = {}
    for i,j in enumerate(nums):
        leave = target - nums[i]
        #在 dict 中尋找
        if leave in dict:
            ans = [i, dict[leave]]
            return ans
        #若找不到則存入
        else :
            dict[j] = i
```  
### 時間複雜度

上面的方法需要跑過 n-1 遍 ，所以為 O(n)。

## Note
假設有以下參數
```python
nums = [1, 10, 100, 1000]
target = 1010
```
我的思考邏輯
```python
當數字為 1 時，在 dict 中找不到 1009，因此放入 dict
-----------
{
    1 : 0
}
-----------

當數字為 10 時，在 dict 中找不到 1000，因此放入 dict
-----------
{
    1 : 0
    10 : 1
}
-----------

當數字為 100 時，在 dict 中找不到 910，因此放入 dict
-----------
{
    1 : 0
    10 : 1
    100 : 2
}
-----------

當數字為 1000 時，在 dict 中可找到10 ，因此回傳
-----------
{
    1 : 0
    10 : 1
    100 : 2
}
-----------
[1,3]
```

