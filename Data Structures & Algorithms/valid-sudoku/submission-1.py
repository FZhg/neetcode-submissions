class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict: Dict[int, set] = defaultdict(set)
        columnDict: Dict[int, set] = defaultdict(set)
        sqaureDict: Dict[int, set] = defaultdict(set)
        n, m = 9, 9
        for i in range(n):
            for j in range(m):
                cell = board[i][j]
                if cell == ".":
                    continue
                try:
                    value = int(cell)
                except ValueError:
                    return False
                if  value > 9 or value < 1:
                    return False
                

                # check for duplicate
                if value in rowDict[i]:
                    return False
                
                if value in columnDict[j]:
                    return False
                
                sqaureIndex = (i // 3) * 3 + j // 3
                if value in sqaureDict[sqaureIndex]:
                    return False

                rowDict[i].add(value)
                columnDict[j].add(value)
                sqaureDict[sqaureIndex].add(value)
        

        return True
