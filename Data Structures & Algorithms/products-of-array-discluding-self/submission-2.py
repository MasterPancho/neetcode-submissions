class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        
        # Get the right product of each component by going through the list from left to right 
        # storing the new result for the next iteration
        left = [1] * len(nums)
        left_ans = 1
        for i in range(len(nums)):
            left[i] = left_ans
            left_ans *= nums[i]

        # Get the right product of each component by going through the list from right to left 
        # storing the new result for the next iteration
        right = [1] * len(nums)
        right_ans = 1
        for i in range(len(right)-1, -1, -1):
            right[i] = right_ans
            right_ans *= nums[i]

        #Get the product of both arrays
        for i in range(len(nums)):
            prod.append(left[i] * right[i])

        return(prod)

