class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        
        num = int(''.join([str(digit) for digit in digits]))
        num += 1

        for digit in str(num):
            res.append(int(digit))
        
        return res

