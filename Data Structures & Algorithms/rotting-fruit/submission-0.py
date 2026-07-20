class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #Keep track of the rotten fruits
        queue = deque()
        total_time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        directions = [[0,-1],[-1,0],[0,1],[1,0]] #L, D, R, U

        #Get all rotten fruits in the queue and count all fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                
                if grid[r][c] == 1:
                    fresh += 1

        #Check the concurrent rotten fruits until no more occur
        while(queue and fresh > 0):

            #BFS: Check the whole level before moving to the next one. 
            for i in range(len(queue)):
                r,c = queue.popleft()

                #Add neighbours to queue
                for dr,dc in directions:
                    row, col = r+dr, c+dc

                    if row < 0 or row >=rows or col < 0 or col >=cols or grid[row][col] != 1:
                        continue

                    #Fruit becomes rotten
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            
            total_time += 1

        if fresh == 0:
            return total_time 
        
        else:
            return -1
        