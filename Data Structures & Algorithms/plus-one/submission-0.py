class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        
        while(carry != 0 and i >= 0):
            digits[i] += carry

            if digits[i] != 10:
                carry = 0
            
            else:
                digits[i] = 0
                i -= 1

        if carry == 1:
            digits.insert(0,1)

        return digits


