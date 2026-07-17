class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        #Go through all the numbers
        for number in nums:
            result = 1
            i = 0

            #Loop to get the product of all numbers except itself.
            while(i != len(nums)):
                if(i != nums.index(number)):
                    result *= nums[i]
                i += 1
            
            output.append(result)
                
        return(output)

            