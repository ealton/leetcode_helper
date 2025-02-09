package trees

import "fmt"

type TreeNode struct {
	Val int

	Left *TreeNode
	Right *TreeNode
}

// For a relgular tree, insert to the left most leaf
func (t *TreeNode) Insert(val int) *TreeNode {
	newNode := &TreeNode{
		Val: val,
	}
	node := t
	for node.Left != nil {
		node = node.Left
	}
	node.Left = newNode
	return newNode
}

// Delete all occurences of val
func (t *TreeNode) Delete(val int) *TreeNode {
	if t == nil {
		return nil
	}
	if t.Val != val {
		t.Left = t.Left.Delete(val)
		t.Right =  t.Right.Delete(val)
		return t
	}
	left := t.Left.Delete(val)
	right := t.Right.Delete(val)
	if left == nil && right == nil {
		return nil
	}
	if left == nil {
		return right
	}
	if right == nil {
		return left
	}
	node := left
	for node.Left != nil {
		node = node.Left
	}
	node.Left = right
	return left
}

func (t *AVLTreeNode) ToJSON() string {
	if t == nil {
		return ""
	}
	left := t.Left.ToJSON()
	right := t.Right.ToJSON()
	return fmt.Sprintf("{\"%v\": {left: %v, right: %v}}", t.Val, left, right)
}

