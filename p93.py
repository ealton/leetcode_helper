from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) < 4:
            return []

        def isValid(starting_index: int, length: int, s: str) -> bool:
            # print(f'isValid: {starting_index} {length}')
            if starting_index >= len(s): return False
            if length == 0: return False
            if length == 1: return True
            # length > 1
            if s[starting_index] == "0": return False
            if length == 3:
                val = int(s[starting_index: starting_index + length])
                if val > 255: return False
            if length > 3:
                return False
            return True

        def printIpAddress(length0: int, length1: int, length2: int, s: str) -> str:
            return s[0:length0] + '.' + \
                s[length0:length0+length1] + '.' + \
                s[length0+length1:length0+length1+length2] + '.' + \
                s[length0+length1+length2:len(s)]

        def helper(segment_length: List[int], s: str):
            # print(f'helper: {segment_length}, {s}')
            total_length = sum(segment_length)
            last_dot_index = -1 if len(segment_length) == 0 else segment_length[-1]
            if total_length >= len(s):
                return
            if len(segment_length) == 2:
                # print(f'has two: {segment_length[0]}, {segment_length[1]}, {len(s) - total_length}')
                if len(s) - total_length > 6:
                    # left over digits are more than 3
                    return

                for i in range(1, 4):
                    if total_length + i >= len(s):
                        break
                    if isValid(total_length, i, s) and isValid(total_length + i, len(s) - total_length - i, s):
                        new_value = printIpAddress(segment_length[0], segment_length[1], i, s)
                        # print(f'adding new value: {new_value} {segment_length[0]} {segment_length[1]}, {i}')
                        result.append(new_value)
            else:
                for i in range(1, 4):
                    if total_length + i >= len(s):
                        break
                    if isValid(total_length, i, s):
                        segment_length.append(i)
                        helper(segment_length, s)
                        segment_length.pop()

        helper([], s)
        return result
