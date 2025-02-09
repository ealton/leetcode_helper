package algorithmsgo

import (
	"fmt"
	"testing"
)

func TestUnionFind(t *testing.T) {
	fmt.Println("Starting TestUnionFind")
	uf := InitInnoUnionFindHeavyFind(5)
	uf.Union(1, 2)
	uf.Union(2, 3)
	uf.Union(1, 3)
	assert(t, uf.Connected(1, 2), true)
	assert(t, uf.Connected(3, 4), false)
}
