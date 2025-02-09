class InnoCircularDeque:

    def __init__(self, k: int):
        self.nums = [0] * (k + 1)
        self.front = 0
        self.end = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = self.decrementIndex(self.front)
        self.nums[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.nums[self.end] = value
        self.end = self.incrementIndex(self.end)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.incrementIndex(self.front)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end = self.decrementIndex(self.end)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[self.decrementIndex(self.end)]

    def isEmpty(self) -> bool:
        return self.front == self.end

    def isFull(self) -> bool:
        t = self.incrementIndex(self.end)
        return t == self.front

    def incrementIndex(self, index: int) -> int:
        if index == len(self.nums) - 1:
            return 0
        return index + 1

    def decrementIndex(self, index: int) -> int:
        if index == 0:
            return len(self.nums) - 1
        return index - 1


class Solution:
    def test(self) -> None:
        q = InnoCircularDeque(3)
        assert q.insertLast(1) is True
        assert q.insertLast(2) is True
        assert q.insertFront(3) is True
        assert q.insertFront(4) is False
        assert q.getRear() == 2
        assert q.isFull() is True
        assert q.deleteLast() is True
        assert q.insertFront(4) is True
        assert q.getFront() == 4
        print("All tests passed")


if __name__ == "__main__":
    Solution().test()
