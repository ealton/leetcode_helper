package algorithmsgo

type InnoCircularQueue[T comparable] struct {
	front int
	back  int
	nums  []T
	size  int
}

// Initializes a circular queue
func InitCircularQueue[T comparable](size int) *InnoCircularQueue[T] {
	q := InnoCircularQueue[T]{
		front: 0, back: 0, nums: make([]T, size), size: size,
	}
	return &q
}

func (q *InnoCircularQueue[T]) incrementIndex(index int) int {
	if index == q.size {
		return 0
	}
	return index + 1
}

func (q *InnoCircularQueue[T]) decrementIndex(index int) int {
	if index == 0 {
		return q.size
	}
	return index - 1
}

// Checks if is full
func (q *InnoCircularQueue[T]) IsFull() bool {
	return q.incrementIndex(q.back) == q.front
}

// Checks if is empty
func (q *InnoCircularQueue[T]) IsEmpty() bool {
	return q.back == q.front
}

// Add to back of queue
func (q *InnoCircularQueue[T]) EnQueue(val T) bool {
	if q.IsFull() {
		return false
	}
	q.nums[q.back] = val
	q.back = q.incrementIndex(q.back)
	return true
}

// Remove from front of queue
func (q *InnoCircularQueue[T]) DeQueue() bool {
	if q.IsEmpty() {
		return false
	}
	q.back = q.decrementIndex(q.back)
	return true
}

// Get the front element
func (q *InnoCircularQueue[T]) Front() T {
	if q.IsEmpty() {
		var emptyVal T
		return emptyVal
	}
	return q.nums[q.front]
}

// Get the rear element
func (q *InnoCircularQueue[T]) Rear() T {
	if q.IsEmpty() {
		var emptyVal T
		return emptyVal
	}
	return q.nums[q.decrementIndex(q.back)]
}
