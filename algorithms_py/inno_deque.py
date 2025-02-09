from typing import List

class InnoDequeueNode:
    def __init__(self, val: int, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class InnoDequeue:

    def __init__(self):
        self.front = None
        self.end = None
        self.size = 0

    def isEmpty(self):
        return self.front == None and self.end == None

    def pushFront(self, val: int):
        if self.isEmpty():
            self.front = self.end = InnoDequeueNode(val, None, None)
        else:
            t = InnoDequeueNode(val, None, self.front)
            self.front.prev = t
            self.front = t
        self.size += 1

    def pushEnd(self, val: int):
        if self.isEmpty():
            self.front = self.end = InnoDequeueNode(val, None, None)
        else:
            t = InnoDequeueNode(val, self.end, None)
            self.end.next = t
            self.end = t
        self.size += 1

    def popFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.end:
            self.front = self.end = None
            self.size = 0
        else:
            self.front = self.front.next
            self.front.prev = None
            self.size -= 1
        return True

    def popEnd(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.end:
            self.front = self.end = None
            self.size = 0
        else:
            self.end = self.end.prev
            self.end.next = None
            self.size -= 1
        return True

    def helper(self):
        pass

    def insert(self, val: int, index: int):
        if self.isEmpty() or index == 0:
            self.pushFront(val)
        elif index >= self.size:
            self.pushEnd(val)
        else:
            node = self.front
            for i in range(index):
                node = node.next
            t = InnoDequeueNode(val, node, node.next)
            node.next = t
            t.next.prev = t

        self.size += 1

    def indexOf(self, val: int) -> int:
        node, ans = self.front, 0
        while node and node.val != val:
            node = node.next
            ans += 1
        return -1 if node == None else ans

    def toList(self) -> List[int]:
        ans = []
        node = self.front
        while node:
            ans.append(node.val)
            node = node.next
        return ans


class Solution:
    def compare_lists(self, list1, list2):
        if len(list1) != len(list2):
            return False
        return all(a == b for a, b in zip(list1, list2))

    def test(self) -> None:
        q = InnoDequeue()
        q.pushFront(1)
        q.pushFront(2)
        assert q.indexOf(2) == 0
        assert q.indexOf(1) == 1
        assert q.indexOf(0) == -1
        assert q.size == 2
        q.pushEnd(4)
        q.pushEnd(5)
        print(q.toList())
        assert self.compare_lists(q.toList(), [2, 1, 4, 5]) is True
        assert q.size == 4
        assert q.popFront() is True
        assert q.popFront() is True
        assert q.popEnd() is True
        assert q.popFront() is True
        print(q.toList())
        assert q.popFront() is False
        print("All tests passed")


if __name__ == "__main__":
    Solution().test()
