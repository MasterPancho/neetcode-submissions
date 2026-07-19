class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left = 0
        longest = 0

        for right in range(len(s)):
            #Keep track of the frequency of each element
            seen[s[right]] += 1
        
            #If in the current window we need more replacements than needed, we shrink it.
            while((right-left+1 - max(seen.values())) > k):
                seen[s[left]] -= 1
                left += 1

            #Store the highest window size
            if(right-left+1 > longest):
                longest = right-left+1

        return(longest)
