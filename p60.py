from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = list("123456789")[0:n]
        result = ""

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            return n * factorial(n - 1)

        while n > 0:
            # print(f"n = {n}")
            if n == 1:
                result += s[0]
                return result

            section_count = n
            section_size = factorial(n-1)
            number_index = 0
            while k > section_size:
                # print(f"k = {k}")
                number_index += 1
                k -= section_size
            result += s[number_index]
            del s[number_index]
            n -= 1
