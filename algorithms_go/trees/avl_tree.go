package trees

import (
	"fmt"
	"strconv"
)

type AVLTreeNode struct {
	Val    int
	Freq   int
	Height int
	Left   *AVLTreeNode
	Right  *AVLTreeNode
}

func (t *AVLTreeNode) GetHeight() int {
	if t == nil {
		return 0
	}
	return t.Height
}

func (t *AVLTreeNode) RotateRight() *AVLTreeNode {
	oldLeft := t.Left
	oldLeftRight := oldLeft.Right

	oldLeft.Right = t
	t.Left = oldLeftRight

	t.Height = 1 + max(t.Left.GetHeight(), t.Right.GetHeight())
	oldLeft.Height = 1 + max(oldLeft.Left.GetHeight(), oldLeft.Right.GetHeight())

	return oldLeft
}

func (t *AVLTreeNode) RotateLeft() *AVLTreeNode {
	oldRight := t.Right
	oldRightLeft := oldRight.Left

	oldRight.Left = t
	t.Right = oldRightLeft

	t.Height = 1 + max(t.Left.GetHeight(), t.Right.GetHeight())
	oldRight.Height = 1 + max(oldRight.Left.GetHeight(), oldRight.Right.GetHeight())

	return oldRight
}

func (t *AVLTreeNode) GetBalance() int {
	if t == nil {
		return 0
	}
	return t.Left.GetHeight() - t.Right.GetHeight()
}

func (t *AVLTreeNode) Insert(val int) *AVLTreeNode {
	// Normal BST insert
	if t == nil {
		return &AVLTreeNode{
			Val:  val,
			Freq: 1,
			Height: 1,
		}
	}
	if t.Val == val {
		t.Freq++
		return t
	} else if val < t.Val {
		t.Left = t.Left.Insert(val)
	} else {
		t.Right = t.Right.Insert(val)
	}
	leftHeight, rightHeight := t.Left.GetHeight(), t.Right.GetHeight()
	t.Height = 1 + max(leftHeight, rightHeight)

	if leftHeight > rightHeight+1 && val < t.Left.Val {
		// left, left: rotateRight
		t = t.RotateRight()
	} else if rightHeight > leftHeight + 1 && val > t.Right.Val {
		// right right: rotateLeft
		t = t.RotateLeft()
	} else if leftHeight > rightHeight+1 && val > t.Left.Val {
		// left, right: left rotateLeft, then rotateRight
		t.Left = t.Left.RotateLeft()
		t = t.RotateRight()
	} else if rightHeight > leftHeight+1 && val < t.Right.Val {
		// right, left: right rotateRight, then rotateLeft
		t.Right = t.Right.RotateRight()
		t = t.RotateLeft()
	}
	
	return t
}

func (t *AVLTreeNode) Delete(val int) *AVLTreeNode {
	if t == nil {
		return t
	}

	if t.Val == val {
		if t.Freq > 1 {
			t.Freq--
			return t
		}

		if t.Left == nil && t.Right == nil {
			return nil
		} else if t.Left == nil && t.Right != nil {
			return t.Right
		} else if t.Left != nil && t.Right == nil {
			return t.Left
		} else {
			// Swap t with leftMost item in right child
			node := t.Right
			for node.Left != nil {
				node = node.Left
			}

			t.Val, node.Val = node.Val, t.Val
			t.Freq, node.Freq = node.Freq, t.Freq
			t.Right = t.Right.Delete(val)
		}
	} else if val > t.Val {
		t.Right = t.Right.Delete(val)
	} else {
		t.Left = t.Left.Delete(val)
	}

	leftHeight, rightHeight := t.Left.GetHeight(), t.Right.GetHeight()
	t.Height = 1 + max(leftHeight, rightHeight)

	if leftHeight > rightHeight + 1 {
		// deleted something on right
		leftNode := t.Left
		leftHeight, rightHeight = leftNode.Left.GetHeight(), leftNode.Right.GetHeight()
		if leftHeight >= rightHeight {
			t = t.RotateRight()
		} else {
			t.Left = leftNode.RotateLeft()
			t = t.RotateRight()
		}
	} else if rightHeight > leftHeight + 1 {
		rightNode := t.Right
		leftHeight, rightHeight = rightNode.Left.GetHeight(), rightNode.Right.GetHeight()
		if rightHeight >= leftHeight {
			t = t.RotateLeft()
		} else {
			t.Right = rightNode.RotateRight()
			t = t.RotateLeft()
		}
	}
	
	return t
}


func (t *AVLTreeNode) InOrder() string {
	if t == nil {
		return ""
	}
	left := t.Left.InOrder()
	right := t.Right.InOrder()
	ans := left
	if left != "" {
		ans = ans + " "
	}
	ans += strconv.Itoa(t.Val)+"/"+strconv.Itoa(t.Height)
	if right != "" {
		ans = ans + " " + right
	}
	return ans
}

func (t *AVLTreeNode) PreOrder() string {
	if t == nil {
		return ""
	}
	ans := strconv.Itoa(t.Val)+"/"+strconv.Itoa(t.Height)
	left := t.Left.PreOrder()
	right := t.Right.PreOrder()

	if left != "" {
		left = " " + left
	}
	if right != "" {
		right = " " + right
	}
	return ans + left + right
}

func (t *TreeNode) ToJSON() string {
	if t == nil {
		return ""
	}
	left := t.Left.ToJSON()
	right := t.Right.ToJSON()
	return fmt.Sprintf("{\"%v\": {left: %v, right: %v}}", t.Val, left, right)
}

