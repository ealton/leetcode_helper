from sortedcontainers import SortedList
from typing import List


def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
    """
    Number of sums within a range. Use bisect method to store cumulative sums
    :param self:
    :param nums:
    :param lower:
    :param upper:
    :return:
    """

    if upper < lower: return 0

    prevSums = SortedList([0])
    cSum = 0
    ans = 0

    for num in nums:
        cSum += num
        rightPos = prevSums.bisect_right(cSum - lower)
        leftPos = prevSums.bisect_left(cSum - upper)
        ans += rightPos - leftPos
        prevSums.add(cSum)

    return ans
