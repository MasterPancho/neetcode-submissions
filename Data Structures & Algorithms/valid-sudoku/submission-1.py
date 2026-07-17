class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        box_hash = defaultdict(set)

        for row in range(9):
            for col in range(9):
                #Cell value
                val = board[row][col]

                #Skip the dots
                if val == ".":
                    continue

                #Get the box indexes
                box = (row//3, col//3)

                #Return false if the value repeats in any of the row/column/box hash sets. Else add the given value to it.
                if val in row_hash[row]:
                    return False 
                row_hash[row].add(val)
                
                if val in col_hash[col]:
                    return False
                col_hash[col].add(val)
                
                if val in box_hash[box]:
                    return False
                box_hash[box].add(val)
                
        return True