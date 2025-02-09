package trees

import (
	"strconv"
)

type BSTNode struct {
	Val   int
	Freq  int
	Left  *BSTNode
	Right *BSTNode
}

// For a relgular tree, insert to the left most leaf
func (t *BSTNode) Insert(val int) *BSTNode {
	if t == nil {
		return &BSTNode{
			Val: val,
		}
	}

	if val < t.Val {
		t.Left = t.Left.Insert(val)
	} else if val > t.Val {
		t.Right = t.Right.Insert(val)
	} else {
		// val == t.Val
		t.Freq++
	}
	return t
}

func (t *BSTNode) Delete(val int) *BSTNode {
	if t == nil {
		return nil
	}
	if val < t.Val {
		t.Left = t.Left.Delete(val)
	} else if val > t.Val {
		t.Right = t.Right.Delete(val)
	} else {
		if t.Left == nil {
			return t.Right
		} else if t.Right == nil {
			return t.Left
		} else {
			// find right candidate:
			parent, node := t, t.Right
			for node.Left != nil {
				parent, node = node, node.Left
			}
			// node.Left is nill
			if node.Right != nil {
				parent.Left = node.Right
			} else {
				parent.Left = nil
			}
			t.Val = node.Val
		}
	}
	return t
}

func (t *BSTNode) InOrder() string {
	if t == nil {
		return ""
	}
	left := t.Left.InOrder()
	right := t.Right.InOrder()
	ans := left
	if left != "" {
		ans = ans + " "
	}
	ans += strconv.Itoa(t.Val)
	if right != "" {
		ans = ans + " " + right
	}
	return ans
}