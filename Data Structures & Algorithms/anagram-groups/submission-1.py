class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Initialize dictionary and output list
        groupDict = {}
        output =[]
        
        # Organize the letters of each word alphabetically and categorize them based on this id.
        for word in strs:
            wordId = "".join(sorted(word))     
            if wordId not in groupDict:
                groupDict[wordId] = []
            groupDict[wordId].append(word)
        
        #Return the dictionary as a list
        return(list(groupDict.values()))

