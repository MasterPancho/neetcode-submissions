class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        largest = tCount
        smallest = sCount

        if(len(s) > len(t)):
            largest = sCount 
            smallest = tCount

        for letter in s:
            sCount[letter] = sCount.get(letter, 0) + 1

        for letter in t:
            tCount[letter] = tCount.get(letter, 0) + 1

        for key in largest:
            if(largest.get(key) != smallest.get(key)):
                return False
        return True
