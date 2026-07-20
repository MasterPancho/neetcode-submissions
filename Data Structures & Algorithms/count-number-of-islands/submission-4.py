class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #No Islands
        if not grid:
            return 0
        
        neighbours = [[0,-1],[-1,0],[0,1],[1,0]]
        visited = set()

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            #No need to repeat the ones already visited    
            if(r,c) in visited:
                return
                
            visited.add((r,c))

            #Check all its neighbours (Left, Down, Right, Up)
            for dr,dc in neighbours:
                #Find the coordinates of the neighbour cell
                nr, nc = r+dr, c+dc       

                #Invalid cell (boundaries)
                if(nr < 0 or nr == rows or nc < 0 or nc == cols):
                    continue

                if grid[nr][nc] == '0':
                    continue

                #If in the given direction theres a new "1", add it to the queue
                dfs(nr, nc)

        #Go through each cell 
        for m in range(rows):
            for n in range(cols):
                if(grid[m][n] == "1" and (m,n) not in visited):
                    dfs(m, n)
                    islands += 1

        return islands




#We could also do it this way:

        # def bfs(r, c):
        #     #Add the cell as visited
        #     visited.add((r,c))

        #     #Check all its neighbours (Left, Down, Right, Up)
        #     for dr, dc in ([0,-1],[-1,0],[0,1],[1,0]):

        #         #New cell
        #         nr, nc = r+dr, c+dc       

        #         #Invalid cell (boundaries)
        #         if(nr == -1 or nr == rows or nc ==-1 or nc == cols):
        #             continue

        #         #If in the given direction theres a new "1", perform bfs on it.
        #         if (grid[nr][nc] == "1" and (nr, nc) not in visited):
        #             bfs(nr, nc)
