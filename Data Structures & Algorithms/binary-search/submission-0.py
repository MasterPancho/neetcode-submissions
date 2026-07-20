class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0  
        high = len(nums) - 1
        mid = high-low

        while(low <= high):
            #Target found
            if(nums[mid] == target):
                return mid

            #All number before mid are ignored and a new mid is calculated
            elif(nums[mid] < target):
                low = mid+1
                mid = high - low

            #All numbers after mid are ignored and a new mid is calculated
            elif(nums[mid] > target):
                high = mid-1
                mid = high-low
        
        return(-1)