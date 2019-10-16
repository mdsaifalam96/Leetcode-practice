BOARD_DIM = 9
GRID_DIM = 3


class Solution:
    def check_grid(self, row_index, col_index, board):
        seen = set()
        for i in range(row_index, row_index + GRID_DIM):
            for k in range(col_index, col_index + GRID_DIM):
                if board[i][k].isnumeric() and board[i][k] in seen:
                    return False
                seen.add(board[i][k])
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for i in range(BOARD_DIM):
            seen = set()
            for k in range(BOARD_DIM):
                if board[i][k].isnumeric() and board[i][k] in seen:
                    return False
                seen.add(board[i][k])

        # check columns
        for i in range(BOARD_DIM):
            seen = set()
            for k in range(BOARD_DIM):
                if board[k][i].isnumeric() and board[k][i] in seen:
                    return False
                seen.add(board[k][i])

        # check grids
        for i in range(BOARD_DIM // GRID_DIM):
            for k in range(BOARD_DIM // GRID_DIM):
                check_result = self.check_grid(
                    i * GRID_DIM, k * GRID_DIM, board)
                if not check_result:
                    return False

        return True


def main():
    solution = Solution()
    sudoku_board_1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert solution.isValidSudoku(sudoku_board_1)
    sudoku_board_2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert not solution.isValidSudoku(sudoku_board_2)


if __name__ == '__main__':
    main()
