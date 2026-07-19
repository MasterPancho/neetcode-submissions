class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0


        for right in range(len(s)):

            #Before adding the character to the set, remove the letters until reaching the given duplicate.           
            while(s[right] in seen):
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            longest = max(longest, len(seen))

        return(longest)
            
        
        
        
        #     if right in range(len(lst)):
        #         remove_index = lst.index(c)
        #         while(remove_index >= 0):
        #             lst.remove(lst[remove_index])
        #             remove_index -= 1
                
        #     lst.append(c)

        #     size = len(lst)
        #     if size > longest:
        #         longest = size

        # return(longest)
