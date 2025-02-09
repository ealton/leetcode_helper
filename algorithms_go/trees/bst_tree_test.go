package trees

import (
	"fmt"
	"testing"
)

func TestBSTNode(t *testing.T) {
	fmt.Println("Starting TestBSTNode")

	root := &BSTNode{
		Val: 50,
	}
	for _, item := range []int{20, 30, 80, 70, 40, 60} {
		root = root.Insert(item)
	}

	fmt.Println(root.InOrder())

	assert(t, root.InOrder(), "20 30 40 50 60 70 80")
	root.Delete(50)
	fmt.Println(root.InOrder())

	assert(t, root.InOrder(), "20 30 40 60 70 80")
}
