package algorithmsgo

import (
	"fmt"
	"testing"
)

func TestInnoTrie(t *testing.T) {
	fmt.Println("Starting TestTrie")
	trie := InitInnoTrie()
	trie.Insert("apple")
	trie.Insert("application")

	assert(t, trie.StartsWith("app"), true)
	assert(t, trie.StartsWith("pp"), false)
	assert(t, trie.Search("application"), true)
	assert(t, trie.Search("apple"), true)
	assert(t, trie.Search("app"), false)
	assert(t, trie.Search("ab"), false)
}
