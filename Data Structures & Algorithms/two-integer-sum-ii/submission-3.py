class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(numbers)-1

        while(low < high):

            #Move top arrow down to get a smaller result 
            if((numbers[low]+numbers[high]) > target):
                high -= 1
            
            #Move lower arrow up to get a greater result 
            elif((numbers[low]+numbers[high]) < target):
                low += 1

            #Return the indexes when the target is reached 
            else:
                return[low+1, high+1]
            

        return None
            