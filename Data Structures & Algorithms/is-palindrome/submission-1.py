class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Remove any non-alphanumeric values and put them in lowercase
        cleaned = "".join(char for char in s if char.isalnum()).lower()
        
        #Read the text backwards and return True if its the same
        return cleaned == cleaned[::-1]