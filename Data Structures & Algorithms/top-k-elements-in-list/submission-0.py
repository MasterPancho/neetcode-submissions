class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}

        #Store the number of times a number repeats in the list
        for number in nums:
            numCount[number] = numCount.get(number,0) + 1

        #Sort the dictionary by the k highest frequent elements. 
        kFrequent = sorted(numCount, key=lambda f: numCount[f], reverse=True)[:k]

        return(kFrequent)