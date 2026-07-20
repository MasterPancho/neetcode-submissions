class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
 
            #While the top is smaller than the one we are going to append, we calculate days, and pop it    
            while(stack and stack[-1][1] < temp):
                days[stack[-1][0]] = index - stack[-1][0]  
                stack.pop()

            #Add temperature with its index to stack
            stack.append((index, temp))


        return(days)

            
