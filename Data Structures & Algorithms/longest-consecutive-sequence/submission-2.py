class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Add to a set, which removes any duplicates
        nums_set = set(nums)
        cur_highest = 0

        #Go through the sorted set
        for num in nums_set:

            #Get the start of a sequence, and check if a sequence exist by continuously incrementing the number by 1
            if (num-1) not in nums_set:
                length = 1
                while((num+length) in nums_set):
                    length += 1

                cur_highest = max(cur_highest, length)                
        
        return(cur_highest)