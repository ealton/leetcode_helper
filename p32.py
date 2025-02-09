class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """


        print(f'Testing string: {s}')

        nested_starting_indices = []
        nested_length = []

        index = 0
        while index < len(s):
            (start_index, length) = Solution.locateInnerMostParentheses(s, index)
            index = start_index + max(1, length)
            if length > 0:
                nested_starting_indices.append(start_index)
                nested_length.append(length)

        if len(nested_length) == 0:
            return 0

        print(f'nested indices and length: {nested_starting_indices} {nested_length}')

        while True:
            has_combined = False
            for i in range(0, len(nested_starting_indices)-1):
                if nested_starting_indices[i] + nested_length[i] == nested_starting_indices[i+1]:
                    print(f'Combine nested_starting_indices: {i} {i+1}')
                    del nested_starting_indices[i+1]
                    nested_length[i] = nested_length[i] + nested_length[i+1]
                    del nested_length[i+1]
                    has_combined = True
                    break

            if has_combined:
                continue

            has_expanded = False
            for i in range(0, len(nested_starting_indices)):
                new_starting_index, new_length = Solution.expandParentheses(s, nested_starting_indices[i], nested_length[i])
                if new_starting_index != nested_starting_indices[i]:
                    nested_starting_indices[i] = new_starting_index
                    nested_length[i] = new_length
                    has_expanded = True
                    break

            if not has_expanded:
                break

        return max(nested_length)

    @staticmethod
    def locateInnerMostParentheses(s, starting_index):
        """
        :param s:
        :param starting_index:
        :return: (startingIndex, length)
        """
        print(f'locateInnerMostParentheses: {starting_index}')
        for i in range(starting_index, len(s)):
            if s[i] == '(':
                continue
            if s[i] == ')' and i > starting_index and s[i-1] == '(':
                print(f'{i-1} {2}')
                return i-1, 2

        print(f'{starting_index} {0}')
        return starting_index, 0

    @staticmethod
    def expandParentheses(s, starting_index, length):
        print(f'expandParentheses: {starting_index} {length}')
        ending_index = starting_index + length - 1

        while starting_index - 1 >= 0 and ending_index + 1 < len(s):
            if s[starting_index-1] == '(' and s[ending_index+1] == ')':
                starting_index -= 1
                ending_index += 1
            else:
                break

        print(f'result: {starting_index} {ending_index-starting_index+1}')
        return starting_index, ending_index - starting_index+1
