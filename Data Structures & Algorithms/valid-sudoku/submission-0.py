class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()

            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False
                
                seen.add(value)
            
        for col in range(9):
            seen = set()
            
            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue
                
                if value in seen:
                    return False
                
                seen.add(value)
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        value = board[row][col]

                        if value == ".":
                            continue
                        
                        if value in seen:
                            return False
                        
                        seen.add(value)
        
        return True

            
        
        



            
        