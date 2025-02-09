from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    freqCache = {}
    cSum = 0
    ans = 0
    for num in nums:
        cSum += num
        if cSum == k:
            # a valid subarray from index 0 to current number
            ans += 1

        complNum = cSum - k
        if complNum in freqCache:
            # how many previous prefix subarrays ends with complNum?
            # foreach one of them, subtract them from the current prefix subarray, then we get a new subarray with sum k
            ans += freqCache[complNum]

        if cSum not in freqCache:
            freqCache[cSum] = 1
        else:
            freqCache[cSum] += 1

    return ans
