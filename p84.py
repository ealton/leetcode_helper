from typing import List


class Solution:

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
