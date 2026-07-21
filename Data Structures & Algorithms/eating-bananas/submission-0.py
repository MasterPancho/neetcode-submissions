class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #boundary of smallest to largest #bananas in the piles
        left, right = 1, max(piles)

        #Koko eats the max number as min by default
        min_res = right

        while(left <= right):
            # #hrs it takes for Koko to eat the piles
            hours = 0

            #Midpoint
            k = (left+right) // 2

            #Koko eats k bananas / hour 
            for p in piles:
                hours += math.ceil(p / k)
            
            #We reached a minimum, thus reduce the range by shifting right pointer down
            if hours <= h:
                min_res = min(min_res, k)                
                right = k-1

            #We need a higher rate, so move left pointer up
            else:
                left = k+1

        return min_res

            