import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        s1 = -prices[0]
        s2 = -sys.maxsize - 1
        s3 = -sys.maxsize - 1
        s4 = -sys.maxsize - 1

        for i in range(len(prices)):
            print(f's1-4: {s1} {s2} {s3} {s4}')
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])

        return max(0, s4)
