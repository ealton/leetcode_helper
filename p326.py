import math


class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        ansW = 3
        print(str(ansW))
        ans = math.log(n, 2) / math.log(3, 2)
        return ans % 1 == 0

    def test(self):
        # print(self.calculate("1 + 1"))
        # print(self.calculate(" 2-1 + 2 "))
        # print(self.calculate(" 4+5+2"))
        # print(self.calculate("1+(4+5+2)"))
        # print(self.calculate("1+(4+5+2)-3"))
        # print(self.calculate("(1+(4+5+2)-3)"))
        # print(self.calculate("(1+(4+5+2)-3)+(6+8)"))
        print(self.isPowerOfThree(-9))
        test = []
        test.extend