class InnoCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.back = 0
        self.nums = [0] * (k + 1)
        self.k = k

    def _incrementIndex(self, index: int) -> int:
        if index == len(self.nums) - 1:
            return 0
        return index + 1

    def _decrementIndex(self, index: int) -> int:
        if index == 0:
            return len(self.nums) - 1
        return index - 1

    def enQueue(self, value: int) -> bool:
        # putting element at end of the queue
        if self.isFull():
            return False
        self.nums[self.back] = value
        self.back = self._incrementIndex(self.back)
        return True

    def deQueue(self) -> bool:
        # remove element from front of the queue
        if self.isEmpty():
            return False
        self.back = self._decrementIndex(self.back)
        return True

    def Front(self) -> int:
        # read first element
        if self.isEmpty():
            return -1
        return self.nums[self.front]

    def Rear(self) -> int:
        # read last element
        if self.isEmpty():
            return -1
        return self.nums[self._decrementIndex(self.back)]

    def isEmpty(self) -> bool:
        # if front equals back, then is empty
        return self.front == self.back

    def isFull(self) -> bool:
        # if adding one additional element will make back to point to front, then is full
        t = self._incrementIndex(self.back)
        return t == self.front


class Solution:
    def test(self) -> None:
        q = InnoCircularQueue(3)
        assert q.enQueue(1) is True
        assert q.enQueue(2) is True
        assert q.enQueue(3) is True
        assert q.enQueue(4) is False
        assert q.Rear() == 3
        assert q.isFull() is True
        assert q.deQueue() is True
        assert q.enQueue(4) is True
        assert q.Rear() == 4
        print("All tests passed")


if __name__ == "__main__":
    Solution().test()
