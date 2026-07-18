class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_list = sorted(nums)
        output = set()

        #Go through each value and use the two-pointer algorithm to find the triplets
        for i in range(len(sorted_list)):
            low = i+1
            high = len(sorted_list)-1

            while(low < high):

                #Check if the total is zero
                total = sorted_list[i] + sorted_list[low] + sorted_list[high] 

                #total > 0, decrement high pointer
                if(total > 0):
                    high -= 1
                
                #total < 0, increment low pointer
                elif(total < 0):
                    low += 1
                
                #Store the result into the set
                else:
                    output.add((sorted_list[i], sorted_list[low], sorted_list[high]))
                    low += 1
                    high-= 1

        return([list(t) for t in output])