package algorithmsgo

import (
	"fmt"
	"testing"
)

func TestTopoSort(t *testing.T) {
	fmt.Println("Starting TestTopoSort")
	conditions := [][]int{}
	conditions = append(conditions, []int{1, 0})
	conditions = append(conditions, []int{2, 0})
	conditions = append(conditions, []int{3, 1})
	conditions = append(conditions, []int{3, 2})
	result := TopoSort(conditions, []int{0, 1, 2, 3})

	fmt.Println(result)

	assert(t, CompareTwoSlices(&result, &[]int{3, 1, 2, 0}), true)
}
