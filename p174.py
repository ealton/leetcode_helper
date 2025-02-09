from typing import List


class Solution:

    def test(self):
        print(self.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
        print(self.calculateMinimumHP([[0]]))
        # a = 0

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        column = len(dungeon[0])

        end_value = dungeon[-1][-1]
        previous_row = [1 - end_value if end_value < 0 else 1] * column
        for c in range(column-2, -1, -1):
            previous_row[c] = max(1, previous_row[c + 1] - dungeon[row-1][c])

        print(previous_row)
        for r in range(row-2, -1, -1):
            current_row = [0] * column
            current_row[-1] = max(1, previous_row[-1] - dungeon[r][-1])

            for c in range(column-2, -1, -1):
                current_row[c] = max(1, min(previous_row[c] - dungeon[r][c], current_row[c+1] - dungeon[r][c]))
            previous_row = current_row

            print(previous_row)

        return previous_row[0]
