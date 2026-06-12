class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[] for box_index in range(9)]       

        for i in range(9):
            if not self.isDuplicate(board[i]):
                return False

        for i in range(9):
            col = [board[row][i] for row in range(9)]
            if not self.isDuplicate(col):
                return False

        for i in range(9):
            for j in range(9):
                box_index = (i//3) * 3 + (j//3)
                boxes[box_index].append(board[i][j])

        for i in range(9):
            if not self.isDuplicate(boxes[i]):
                return False

        return True
        
    def isDuplicate(self, valid: List[str]) -> bool:
        s = set()

        for i in range(len(valid)):
            if valid[i] == '.':
                continue
            if valid[i] in s:
                return False
            else: s.add(valid[i])
        return True
