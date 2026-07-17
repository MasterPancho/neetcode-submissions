class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        if(len(s) != len(t)):
            return False
            
        for letter in s:
            sCount[letter] = sCount.get(letter, 0) + 1

        for letter in t:
            tCount[letter] = tCount.get(letter, 0) + 1

        for key in sCount:
            if(sCount.get(key) != tCount.get(key)):
                return False
        return True
