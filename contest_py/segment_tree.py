from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * self.n * 2

        i, j = self.n, 0
        while i < self.n * 2:
            self.tree[i] = nums[j]
            i, j = i + 1, j + 1

        for k in range(self.n - 1, 0, -1):
            self.tree[k] = self.tree[k * 2] + self.tree[k * 2 + 1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val

        while index > 0:
            l = index
            r = index
            if index % 2 == 0:
                r = index + 1
            else:
                l = index - 1
            self.tree[index // 2] = self.tree[l] + self.tree[r]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n
        ans = 0
        while l <= r:
            if l % 2 == 1:
                ans += self.tree[l]
                l += 1
            if r % 2 == 0:
                ans += self.tree[r]
                r -= 1

            l //= 2
            r //= 2

        return ans
