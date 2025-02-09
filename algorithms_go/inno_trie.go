package algorithmsgo

type InnoTrieNode struct {
	childMap map[rune]*InnoTrieNode
	isEnd    bool
}

func InniInnoTrieNode() *InnoTrieNode {
	node := InnoTrieNode{
		childMap: make(map[rune]*InnoTrieNode),
		isEnd:    false,
	}
	return &node
}

type InnoTrie struct {
	root *InnoTrieNode
}

func InitInnoTrie() *InnoTrie {
	trie := InnoTrie{
		root: InniInnoTrieNode(),
	}
	return &trie
}

func (t *InnoTrie) Insert(word string) {
	current := t.root
	for _, c := range word {
		child, exists := (*current).childMap[c]
		if exists {
			current = child
		} else {
			newNode := InniInnoTrieNode()
			(*current).childMap[c] = newNode
			current = newNode
		}
	}
	current.isEnd = true
}

func (t *InnoTrie) Search(word string) bool {
	current := t.root
	for _, c := range word {
		child, exists := current.childMap[c]
		if !exists {
			return false
		}
		current = child
	}
	return current.isEnd
}

func (t *InnoTrie) StartsWith(prefix string) bool {
	current := t.root
	for _, c := range prefix {
		child, exists := current.childMap[c]
		if !exists {
			return false
		}
		current = child
	}
	return true
}
