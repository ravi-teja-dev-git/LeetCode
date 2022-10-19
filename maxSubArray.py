class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = -999999
        sum1 = 0
        for i in range(0,len(nums)):
            sum1 = sum1 + nums[i]
            if sum1 > maxNum:
                maxNum = sum1
            if sum1<0:
                sum1 = 0
                
        return maxNum
                
        