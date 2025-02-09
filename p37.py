from typing import List


class Solution(object):
    isDebug = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        result, solved_board = self.solveBoard(board)
        if not result:
            print("Error, board not solved")
        for i in range(9):
            for j in range(9):
                board[i][j] = solved_board[i][j]

    def solveBoard(self, board: List[List[str]]) -> (bool, List[List[str]]):
        board_impossible_values = []
        for i in range(9):
            row = [[] for j in board[i]]
            board_impossible_values.append(row)

        while True:
            if self.isBoardFilled(board):
                break
            made_progress = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        continue

                    candidates = self.getCellCandidates(board, i, j, board_impossible_values)
                    if self.isDebug:
                        print(f"{i}, {j} candidates: {candidates}")
                    if len(candidates) <= 0:
                        return False, None

                    if len(candidates) == 1:
                        if self.isDebug:
                            print(f"Made progress {i}, {j} = {candidates[0]}")
                        made_progress = True
                        board[i][j] = candidates[0]

            if made_progress:
                continue

            if self.isDebug:
                print("Has not made progress")

            duplicated_board = self.duplicateBoard(board)
            target_row, target_column, guessing_value = self.makeEducatedGuess(board, board_impossible_values)
            duplicated_board[target_row][target_column] = guessing_value

            if self.isDebug:
                print(f"Made a guess: {target_row}, {target_column} = {duplicated_board[target_row][target_column]}")
            solved, result_board = self.solveBoard(duplicated_board)
            if solved:
                board = result_board
                break
            else:
                if self.isDebug:
                    print(f"Eliminated a value: {target_row}, {target_column} != {duplicated_board[target_row][target_column]}")
                board[target_row][target_column] = "."
                board_impossible_values[target_row][target_column].append(guessing_value)

        return True, board

    def getFirstEmptyCell(self, board: List[List[str]]) -> (int, int):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i, j
        print("Error: non empty cell found")
        return -1, -1

    def getCellCandidates(self, board: List[List[str]], row_index: int, column_index: int, board_impossible_values: List[List[List[str]]]) -> List[str]:
        candidates = []
        for num in [str(i+1) for i in range(9)]:
            if self.hasValueInRow(board, row_index, num):
                continue
            if self.hasValueInColumn(board, column_index, num):
                continue
            if self.hasValueInSquare(board, row_index, column_index, num):
                continue
            if num in board_impossible_values[row_index][column_index]:
                continue
            candidates.append(num)

        return candidates

    def hasValueInRow(self, board: List[List[str]], row_index: int, target_value: str) -> bool:
        for i in range(9):
            if board[row_index][i] == target_value:
                return True
        return False

    def hasValueInColumn(self, board: List[List[str]], column_index: int, target_value: str) -> bool:
        for i in range(9):
            if board[i][column_index] == target_value:
                return True
        return False

    def hasValueInSquare(self, board: List[List[str]], row_index: int, column_index: int, target_value: str) -> bool:
        starting_row_index = row_index // 3 * 3
        starting_column_index = column_index // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[starting_row_index + i][starting_column_index+j] == target_value:
                    return True
        return False

    def isTargetValueFilled(self, board: List[List[str]], target_value: str) -> bool:
        target_value_num = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == target_value:
                    target_value_num += 1
        return target_value_num >= 9

    def isBoardFilled(self, board: List[List[str]]):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return False
        return True

    def duplicateBoard(self, board: List[List[str]]):
        new_board = []
        for i in range(9):
            row = [j for j in board[i]]
            new_board.append(row)
        return new_board

    def makeEducatedGuess(self, board: List[List[str]], impossible_values: List[List[List[str]]]):
        least_candidate_row_index = 0
        least_candidate_column_index = 0
        least_candidate_count = 10
        guess = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    continue

                candidates = self.getCellCandidates(board, i, j, impossible_values)
                if len(candidates) < least_candidate_count:
                    least_candidate_row_index = i
                    least_candidate_column_index = j
                    least_candidate_count = len(candidates)
                    guess = candidates[0]
        return least_candidate_row_index, least_candidate_column_index, guess

