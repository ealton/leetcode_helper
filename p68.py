import math
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_count = len(words)
        result = []
        current_line = []
        current_line_letter_count = 0
        i = 0

        while i < words_count:
            if current_line_letter_count + len(current_line) + len(words[i]) > maxWidth:
                space_count = maxWidth - current_line_letter_count
                # print(f"current line = {current_line} + {space_count}")
                current_line_word_count = len(current_line)
                current_line_string = ''
                if current_line_word_count == 1:
                    result.append(current_line[0] + ' ' * space_count)
                else:
                    for j in range(current_line_word_count):
                        current_line_string += current_line[j]
                        if j < current_line_word_count - 1:
                            space_num = math.ceil(space_count / (current_line_word_count - 1 - j))
                            current_line_string += ' ' * space_num
                            space_count -= space_num
                    result.append(current_line_string)
                current_line = []
                current_line_letter_count = 0

            current_line.append(words[i])
            current_line_letter_count += len(words[i])

            if i == words_count - 1:
                result.append(' '.join(current_line) + ' ' * (maxWidth - current_line_letter_count - (len(current_line) - 1)))

            i += 1

        return result

