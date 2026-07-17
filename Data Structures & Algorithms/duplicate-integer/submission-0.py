class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Dictionary
        counter={}

        #Go through each number
        for number in nums:

            #Store it in the dictionary. Key is the number, and its value is the number of times it appears.
            counter[number] = counter.get(number, 0) + 1
        
        for key in counter:
            if(counter[key] > 1):
                return True    
        return False