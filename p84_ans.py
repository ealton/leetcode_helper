from typing import List


class Solution:

    isDebug = False
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0
        length = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
            print(stack)

        for i, h in stack:
            max_area = max(max_area, h * (length - i))
        return max_area
