package algorithmsgo

import (
	"fmt"
	"log"
	"sort"
	"testing"
)

func TestSlices(t *testing.T) {
	fmt.Println("Starting TestSlices")
	s1 := []int{
		1, 3, 9, 2, 3, 5, 4, 3, 2, 6, 1,
	}
	s2 := []int{
		1, 3, 9, 2, 5, 4, 6,
	}

	CompareTwoSlices(RemoveDuplicateInSlice(&s1), &s2)

	s1 = []int{
		// 3, 4, 1, 5, 6, 4, 3, 4, 6, 7, 8, 2, 4, 4, 6,
		2, 1,
	}

	s1Sorted := SortSlice(&s1)
	s1Sorted2 := sort.IntSlice(s1)
	s1Sorted2.Sort()
	log.Println("S1Sorted=", s1Sorted)
	// CompareTwoSlices[int](s1Sorted2, s1Sorted)
}
