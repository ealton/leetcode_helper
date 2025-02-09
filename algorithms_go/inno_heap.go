package algorithmsgo

import (
	"container/heap"

	"golang.org/x/exp/constraints"
)

// Golang's container/heap package only provides a interface
// We need to implement all of heap's methods in order to use it,
// Namely, the Len, Less, Swap, Push, and Pop methods
// Below are an example implementations
type InnoHeap[T constraints.Ordered] []T

func (h InnoHeap[T]) Len() int               { return len(h) }
func (h InnoHeap[T]) Less(i int, j int) bool { return h[i] < h[j] }
func (h InnoHeap[T]) Swap(i int, j int)      { h[i], h[j] = h[j], h[i] }
func (h *InnoHeap[T]) Push(x any)            { *h = append(*h, x.(T)) }
func (h *InnoHeap[T]) Pop() any {
	temp := *h
	x := temp[len(temp)-1]
	*h = temp[:len(temp)-1]
	return x
}

// Usage:
func example1() {
	minHeap := &InnoHeap[int]{}
	heap.Push(minHeap, 3)
	heap.Push(minHeap, 4)
	_ = heap.Pop(minHeap)
	// minHeap.Peek()
}

type InnoHeapInt []int

func (h InnoHeapInt) Len() int           { return len(h) }
func (h InnoHeapInt) Less(i, j int) bool { return h[i] < h[j] }
func (h InnoHeapInt) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *InnoHeapInt) Push(x any)        { *h = append(*h, x.(int)) }
func (h *InnoHeapInt) Pop() any {
	temp := *h
	x := temp[len(temp)-1]
	*h = temp[:len(temp)-1]
	return x
}
