def func():
    n = int(input())
    if n<=1:
        return
    nums = list(map(int,input().split()))
    for i in range(1,n):
        min = float('inf')
        minIndex = -1
        for j in range(i):
            res = abs(nums[i]-nums[j])
            if res<min:
                min = res
                minIndex=j
        print(min,minIndex)
func()