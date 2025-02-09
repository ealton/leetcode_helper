package algorithmsgo

// Topological sorting is an algorithm that can be used to
// help select courses by ensuring that courses are taken 
// in the correct order

func TopoSort[T comparable](conditions [][]T, vocab []T) []T {
	// use a map for fast vocab existence check
	vocabMap := make(map[T]bool)
	for _, v := range vocab {
		vocabMap[v] = true
	}

	childMap := make(map[T][]T)
	inDegree := make(map[T]int)
	for _, cond := range conditions {
		u, v := cond[0], cond[1]
		childMap[u] = append(childMap[u], v)
		inDegree[v]++
	}

	q := []T{}
	ans := []T{}
	for _, v := range vocab {
		if inDegree[v] == 0 {
			q = append(q, v)
		}
	}

	for len(q) > 0 {
		letter := q[0]
		q = q[1:]
		ans = append(ans, letter)
		children := childMap[letter]
		for _, child := range children {
			inDegree[child] -= 1
			if inDegree[child] == 0 {
				q = append(q, child)
			}
		}
	}

	return ans
}
