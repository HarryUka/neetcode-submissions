class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visitedRows = collections.defaultdict(set)
        visitedCols = collections.defaultdict(set)
        visitedSquare = collections.defaultdict(set)


        rows , cols = len(board) , len(board[0])

        for r in range(rows):
            for c in range(cols):
                node = board[r][c]
                if node == ".":
                    continue 
                if (node in visitedRows[r]) or (node  in visitedCols[c]) or (node  in visitedSquare[(r//3,c//3)]):
                    return False
                visitedRows[r].add(node)
                visitedCols[c].add(node)
                visitedSquare[(r//3,c//3)].add(node)

        return True 
                 
        