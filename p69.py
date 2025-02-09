class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        if x == 1:
            return 1
        min_v = 1
        max_v = x

        while True:
            mid = (max_v + min_v) // 2
            # print(f"min, max, mid: {min_v} {max_v} {mid}")
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                max_v = mid - 1
                continue
            if mid * mid < x:
                min_v = mid + 1
                continue

