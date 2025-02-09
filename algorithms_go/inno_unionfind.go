package algorithmsgo

import "fmt"

type InnoUnionFindHeavyFind struct {
	root []int
}

// Initializes a union find
func InitInnoUnionFindHeavyFind(size int) *InnoUnionFindHeavyFind {
	root := make([]int, size)
	for i := 0; i < size; i++ {
		root[i] = i
	}
	return &InnoUnionFindHeavyFind{root: root}
}

// Find the root node of x
func (uf *InnoUnionFindHeavyFind) Find(x int) int {
	return (*uf).root[x]
}

// Connect y into x
func (uf *InnoUnionFindHeavyFind) Union(x int, y int) bool {
	fx, fy := uf.Find(x), uf.Find(y)
	if fx == fy {
		return false
	}
	n := len(uf.root)
	for i := 0; i < n; i++ {
		if uf.root[i] == fy {
			uf.root[i] = fx
		}
	}
	return true
}

// Checks to see if x and y are connected
func (uf *InnoUnionFindHeavyFind) Connected(x int, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

// Get number of components
func (uf *InnoUnionFindHeavyFind) ComponentCount() int {
	ans := 0
	for i, item := range uf.root {
		if i == item {
			ans += 1
		}
	}
	return ans
}

// Prints the root
func (uf *InnoUnionFindHeavyFind) PrintRoot() {
	fmt.Println(uf.root)
}

type InnoUnionFindHeavyUnion struct {
	root []int
}

// Initializes a union find
func InitInnoUnionFindHeavyUnion(size int) *InnoUnionFindHeavyUnion {
	root := make([]int, size)
	for i := 0; i < size; i++ {
		root[i] = i
	}
	return &InnoUnionFindHeavyUnion{root: root}
}

// Find root
func (uf *InnoUnionFindHeavyUnion) Find(x int) int {
	if uf.root[x] == x {
		return x
	}
	uf.root[x] = uf.Find(uf.root[x])
	return uf.root[x]
}

// Union two components
func (uf *InnoUnionFindHeavyUnion) Union(x int, y int) bool {
	fx, fy := uf.Find(x), uf.Find(y)
	if fx == fy {
		return false
	}
	uf.root[fy] = x
	return true
}

// Checks if two nodes are connected
func (uf *InnoUnionFindHeavyUnion) Connected(x int, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

// Get component count
func (uf *InnoUnionFindHeavyUnion) ComponnetCount() int {
	ans := 0
	for i, item := range uf.root {
		if i == item {
			ans += 1
		}
	}
	return ans
}

// Print
func (uf *InnoUnionFindHeavyUnion) PrintRoots() {
	fmt.Println(uf.root)
}

type InnoUnionFindByRank struct {
	root []int
	rank []int
}

// Initializes a union find
func InitInnoUnionFindByRank(size int) *InnoUnionFindByRank {
	root := make([]int, size)
	rank := make([]int, size)
	for i := 0; i < size; i++ {
		root[i] = i
		rank[i] = 1
	}
	return &InnoUnionFindByRank{root: root, rank: rank}
}

// Find root
func (uf *InnoUnionFindByRank) Find(x int) int {
	for x != uf.root[x] {
		x = uf.root[x]
	}
	return x
}

// Union two components
func (uf *InnoUnionFindByRank) Union(x int, y int) bool {
	rootX, rootY := uf.Find(x), uf.Find(y)
	if rootX == rootY {
		return false
	}
	if uf.rank[rootX] > uf.rank[rootY] {
		uf.root[rootY] = rootX
	} else if uf.rank[rootX] < uf.rank[rootY] {
		uf.root[rootX] = rootY
	} else {
		uf.root[rootY] = rootX
		uf.rank[rootX]++
	}

	return true
}

// Checks if two nodes are connected
func (uf *InnoUnionFindByRank) Connected(x int, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

// Get component count
func (uf *InnoUnionFindByRank) ComponnetCount() int {
	ans := 0
	for i, item := range uf.root {
		if i == item {
			ans += 1
		}
	}
	return ans
}

// Print
func (uf *InnoUnionFindByRank) PrintRoots() {
	fmt.Println(uf.root)
}
