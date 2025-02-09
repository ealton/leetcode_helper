from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        width = len(matrix[0])
        height = len(matrix)
        previous_row = [0] * width
        current_row = [0] * width
        max_area = 0

        for r in range(height):
            for c in range(width):
                current_row[c] = 1 if matrix[r][c] == '1' else 0
            for c in range(width):
                if current_row[c] > 0:
                    current_row[c] += previous_row[c]
                previous_row[c] = current_row[c]
            max_area = max(max_area, self.largestRectangleArea(current_row))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # starting_indices = []
        # starting_indices_heights = []
        stack = []
        max_area = 0

        for i in range(len(heights)):
            h = heights[i]
            start = i
            while len(stack) > 0 and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))
        for i in range(len(stack)):
            max_area = max(max_area, (len(heights) - stack[i][0]) * stack[i][1])

        return max_area
