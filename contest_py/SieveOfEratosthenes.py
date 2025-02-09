from typing import List


def sieveOfEratosthenes(target: int) -> List[int]:
    isPrime = [True] * target
    isPrime[0] = False
    isPrime[1] = False

    currentIndex = 1
    while currentIndex < target:
        while currentIndex < target and not isPrime[currentIndex]:
            currentIndex += 1

        currentNum = currentIndex * 2
        while currentNum < target:
            isPrime[currentNum] = False
            currentNum += currentIndex
        currentIndex += 1

    ans = []
    for i in range(target):
        if isPrime[i]:
            ans.append(i)

    return ans
