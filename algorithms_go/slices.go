package algorithmsgo

import "slices"

// Removes duplicates in slice,
// len of slice will shrink if duplicates are found
func RemoveDuplicateInSlice[T comparable](slice *[]T) *[]T {
	seen := map[T]bool{}
	ans := []T{}
	for _, item := range *slice {
		if seen[item] {
			continue
		}
		seen[item] = true
		ans = append(ans, item)
	}
	return &ans
}

// Compare two slices element-wise
// returns true if lengths are identical and each element pair is identical
func CompareTwoSlices[T comparable](slice1 *[]T, slice2 *[]T) bool {
	n := len(*slice1)
	if n != len(*slice2) {
		return false
	}
	for i := 0; i < n; i++ {
		if (*slice1)[i] != (*slice2)[i] {
			return false
		}
	}
	return true
}

func SliceContains[T comparable](needle T, haystack *[]T) bool {
	for i := 0; i < len(*haystack); i++ {
		if (*haystack)[i] == needle {
			return true
		}
	}
	return false
}

func SortSlice[T int | int64 | uint | uint64](s *[]T) *[]T {
	// Different sorting algorithms
	// 1. Selection sort. (select the min from remaining numbers and repeat for n times O(n^2))
	// 2. Insert sort. (find the target location for each num, O(n) to O(n^2))
	// 3. Quick sort. (divide and conquer, O(nlogn), divide to two parts, and merge them, top-down approach)
	// 4. Merge sort. (divide and conquer, O(nlogn), starts from 1, merge and merge, bottom-up approach)
	// 5. Heap sort. (priority queue, minHeap, O(nlogn))
	// 6. Radix sort. (sort based on digits, O(n*d), where d is the number of digits in the largest number)
	// 7. Bubble sort. (opposite of insert sort, O(n^2))
	// 8. Cocktail shake sort. (going back and forth, moving min/max to end/front of array on each pass)
	if len(*s) == 0 {
		return &[]T{}
	}
	if len(*s) == 1 {
		return s
	}

	min := slices.Min(*s)
	max := slices.Max(*s)
	pivot := (min + max) / 2

	s1 := []T{}
	s2 := []T{}
	for _, item := range *s {
		if item <= pivot {
			s1 = append(s1, item)
		} else {
			s2 = append(s2, item)
		}
	}
	smaller := SortSlice(&s1)
	bigger := SortSlice(&s2)

	i1, i2 := 0, 0
	ans := []T{}
	for i1 < len(*smaller) || i2 < len(*bigger) {
		if i1 >= len(*smaller) {
			ans = append(ans, (*bigger)[i2])
			i2++
		} else if i2 >= len(*bigger) {
			ans = append(ans, (*smaller)[i1])
			i1++
		} else if (*smaller)[i1] < (*bigger)[i2] {
			ans = append(ans, (*smaller)[i1])
			i1++
		} else {
			ans = append(ans, (*bigger)[i2])
			i2++
		}
	}
	return &ans
}
