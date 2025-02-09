from typing import List


class Solution:

    def test(self):
        print(self.shortestPalindrome('aacecaaa'))
        # print(self.shortestPalindrome('abcd'))
        # print(self.shortestPalindrome('aaaaa'))
        # print(self.calculateMinimumHP([[0]]))
        # a = 0

    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        mid = len(s) // 2
        first_part_reversed = s[:mid][::-1]
        second_part = s[mid:]
        while len(first_part_reversed) > 0:
            print(f'parts: {first_part_reversed} {second_part}')
            if first_part_reversed == second_part[1:len(first_part_reversed)+1]:
                return second_part[len(first_part_reversed)+1:][::-1] + s
            if first_part_reversed == second_part[0:len(first_part_reversed)]:
                return second_part[len(first_part_reversed):][::-1] + s
            second_part = first_part_reversed[0] + second_part
            first_part_reversed = first_part_reversed[1:]
        return s[1:][::-1] + s


