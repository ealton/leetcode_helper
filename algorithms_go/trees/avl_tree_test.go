package trees

import (
	"fmt"
	"testing"
)

func TestAVLNode(t *testing.T) {
	fmt.Println("Starting TestAVLNode")

	root := &AVLTreeNode{
		Val: 10,
	}
	for _, item := range []int{20, 30, 40, 50, 25} {
		root = root.Insert(item)
		fmt.Println(root.PreOrder())
		fmt.Println("Completed for", item)
	}

	fmt.Println(root.PreOrder())
	fmt.Println(root.InOrder())
	fmt.Println(root.ToJSON())

	assert(t, root.PreOrder(), "20 30 40 50 60 70 80")
	root.Delete(50)
	fmt.Println(root.PreOrder())

	assert(t, root.PreOrder(),"20 30 40 60 70 80")
}
