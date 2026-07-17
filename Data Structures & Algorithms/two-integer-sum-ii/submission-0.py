class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i,num in enumerate(numbers):
            need = target - num

            print(need)

            if need in seen:
                print("A")
                return [seen[need]+1, i+1]         

            else:
                seen[num] = i