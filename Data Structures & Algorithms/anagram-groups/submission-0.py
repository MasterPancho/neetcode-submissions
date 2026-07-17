class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupDict = {}
        output =[]
        for word in strs:
            id = "".join(sorted(word))     
            if id not in groupDict:
                groupDict[id] = []

            groupDict[id].append(word)
        
        for key in groupDict:
            output.append(groupDict[key])
        
        return(output)
