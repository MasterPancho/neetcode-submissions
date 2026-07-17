class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while(i < j):
            
            #Skip non-alphanumeric values and increment the left pointer
            while(i < j and not s[i].isalnum()):
                i += 1

            #Skip non-alphanumeric values and increment the right pointer
            while(i < j and not s[j].isalnum()):
                j -= 1
   
            #Check that both letters are the same
            if(s[i].lower() != s[j].lower()):
                return False
            
            #Increase pointers
            i += 1
            j -= 1

        return True