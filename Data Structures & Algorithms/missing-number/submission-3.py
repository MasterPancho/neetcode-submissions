class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        
        for n in range(size):
            if n not in nums:
                return n
            
        if n+1 not in nums:
            return n+1