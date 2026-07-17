class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i,num in enumerate(numbers):
            need = target - num

            if need in seen:
                return [seen[need]+1, i+1]         

            else:
                seen[num] = i