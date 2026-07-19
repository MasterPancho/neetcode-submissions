class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for char in s:
            #Check the keys
            if char in pairs:

                #Bracket is not closed correctly 
                if not stack or stack[-1] != pairs[char]:
                    return False
                
                #Remove the bracket
                stack.pop()

            #Add the opening brackets            
            else:
                stack.append(char)

        #True if empty
        return (not stack)