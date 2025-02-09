package trees

import (
	"fmt"
	"testing"
)

func TestTreeNode(t *testing.T) {
	fmt.Println("Starting TreeNodeTest")

	root := &TreeNode{
		Val: 3,
	}
	root.Insert(3)
	root.Insert(6)
	root.Insert(9)
	root.Insert(10)
	root.Insert(0)
	root = root.Delete(3)
	root = root.Delete(9)

	fmt.Println(root.ToJSON())
	assertNotEqual(t, root.ToJSON(), "")
}
