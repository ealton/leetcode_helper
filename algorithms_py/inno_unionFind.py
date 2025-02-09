class UnionFindV1HeavyFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def _find(self, x: int) -> int:
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        fx, fy = self._find(x), self._find(y)
        if fx == fy:
            return False
        for i in range(len(self.root)):
            if self.root[i] == fy:
                self.root[i] = fx
        return True

    def connected(self, x: int, y: int) -> bool:
        return self._find(x) == self._find(y)

    def componentCount(self) -> int:
        ans = 0
        for i, item in enumerate(self.root):
            if i == item:
                ans += 1
        return ans

    def printRoots(self):
        print(self.root)


class UnionFindV2HeavyUnion:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def _find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        # flattens the tree
        self.root[x] = self._find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        fx, fy = self._find(x), self._find(y)
        if fx == fy:
            return False
        self.root[fy] = x
        return True

    def connected(self, x: int, y: int) -> bool:
        return self._find(x) == self._find(y)

    def componentCount(self) -> int:
        ans = 0
        for i, item in enumerate(self.root):
            if i == item:
                ans += 1
        return ans

    def printRoots(self):
        print(self.root)


class UnionFindV3ByRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def componentCount(self) -> int:
        ans = 0
        for i, item in enumerate(self.root):
            if i == item:
                ans += 1
        return ans

    def printRoots(self):
        print(self.root)
