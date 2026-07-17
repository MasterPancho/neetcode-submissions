class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {}
        col_hash = {}
        box_hash = {}


        for row in range(9):
            #Create the set for each row
            row_hash[row] = set()

            for col in range(9):
                #Cell value
                val = board[row][col]

                #Skip the dots.
                if val == ".":
                    continue

                #Get the box indexes
                box = (row//3, col//3)
                    
                #Create the set for each column
                if not col in col_hash:
                    col_hash[col] = set()

                #Create the set for each box
                if not box in box_hash:
                    box_hash[box] = set()

                #Return false if the value repeats in any of the given hash sets
                if val in row_hash[row] or val in col_hash[col] or val in box_hash[box]:
                    return False 
                
                #Add the value to the respective hash key   
                else:
                    row_hash[row].add(val)
                    col_hash[col].add(val)
                    box_hash[box].add(val)

        return True