class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cn = self.root
        for c in word:
            if c not in cn.children:
                cn.children[c] = TrieNode()
            cn = cn.children[c]
        cn.isEnd = True

    def search(self, word: str) -> bool:
        cn = self.root
        for c in word:
            if c not in cn.children:
                return False
            cn = cn.children[c]
        return cn.isEnd

    def startsWith(self, prefix: str) -> bool:
        cn = self.root
        for c in prefix:
            if c not in cn.children:
                return False
            cn = cn.children[c]
        return True
