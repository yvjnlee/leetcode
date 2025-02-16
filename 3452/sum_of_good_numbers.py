class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):            
            lower = nums[i-k] if i >= k else 0
            upper = nums[i+k] if i + k < len(nums) else 0

            if nums[i] > lower and nums[i] > upper:
                res += nums[i]

        return res
