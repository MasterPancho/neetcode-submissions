class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #No Islands
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            #Add the cell as visited
            visited.add((r,c))

            #Check all its neighbours (Left, Down, Right, Up)
            for dr, dc in ([0,-1],[-1,0],[0,1],[1,0]):

                #New cell
                nr, nc = r+dr, c+dc       

                #Invalid cell (boundaries)
                if(nr == -1 or nr == rows or nc ==-1 or nc == cols):
                    continue

                #If in the given direction theres a new "1", perform bfs on it.
                if (grid[nr][nc] == "1" and (nr, nc) not in visited):
                    bfs(nr, nc)

        #Go through each cell 
        for m in range(rows):
            for n in range(cols):
                if(grid[m][n] == "1" and (m,n) not in visited):
                    bfs(m, n)
                    islands += 1

        return islands


