class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        #Set the number as the key and the index as its value on the dictionary
        for index, number in enumerate(nums):

            #The number we want to look for to reach target.
            required = target - number
            
            #If the number is on the dictionary, return both indexes
            if(required in seen):
                return[seen.get(required), index]

            #Add the current number to the list
            seen[number] = index
