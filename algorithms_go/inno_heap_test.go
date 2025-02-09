package algorithmsgo

import (
	"container/heap"
	"fmt"
	"testing"
)

func TestHeap(t *testing.T) {
	fmt.Println("Starting TestHeap")
	minHeap := &InnoHeap[int]{}
	heap.Push(minHeap, 10)
	heap.Push(minHeap, 4)
	heap.Push(minHeap, 8)
	assert(t, heap.Pop(minHeap), 4)
	assert(t, heap.Pop(minHeap), 8)
	heap.Push(minHeap, 5)
	assert(t, heap.Pop(minHeap), 5)
	assert(t, heap.Pop(minHeap), 10)
}

func TestHeapInt(t *testing.T) {
	fmt.Println("Starting TestHeap")
	minHeap := &InnoHeapInt{}
	heap.Push(minHeap, 10)
	heap.Push(minHeap, 4)
	heap.Push(minHeap, 8)
	assert(t, heap.Pop(minHeap), 4)
	assert(t, heap.Pop(minHeap), 8)
	heap.Push(minHeap, 5)
	assert(t, heap.Pop(minHeap), 5)
	assert(t, heap.Pop(minHeap), 10)
}
