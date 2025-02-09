package algorithmsgo

type InnoDequeNode[T comparable] struct {
	val  T
	prev *InnoDequeNode[T]
	next *InnoDequeNode[T]
}

// Double-Ended Queue (a double-linked list)
// Push, Pop: O(1)
// Insert at i: O(n)
// IndexOf: O(n)
type InnoDeque[T comparable] struct {
	front *InnoDequeNode[T]
	end   *InnoDequeNode[T]
	size  int
}

// Initialized a deque
func InitInnoDeque[T comparable]() *InnoDeque[T] {
	q := InnoDeque[T]{
		front: nil,
		end:   nil,
		size:  0,
	}
	return &q
}

// Check if is empty
func (q *InnoDeque[T]) IsEmpty() bool {
	return q.end == nil
}

// Push to front
func (q *InnoDeque[T]) PushFront(val T) {
	t := InnoDequeNode[T]{
		val:  val,
		prev: nil,
		next: q.front,
	}
	if q.IsEmpty() {
		q.front = &t
		q.end = &t
	} else {
		q.front.prev = &t
		q.front = q.front.prev
	}
	q.size += 1
}

// Push to end
func (q *InnoDeque[T]) PushEnd(val T) {
	t := InnoDequeNode[T]{
		val:  val,
		prev: q.end,
		next: nil,
	}
	if q.IsEmpty() {
		q.front = &t
		q.end = &t
	} else {
		q.end.next = &t
		q.end = q.end.next
	}
	q.size += 1
}

// Pop from front
func (q *InnoDeque[T]) PopFront() bool {
	if q.IsEmpty() {
		return false
	} else if q.front == q.end {
		q.front = nil
		q.end = nil
	} else {
		q.front = q.front.next
		q.front.prev = nil
	}
	q.size -= 1
	return true
}

// Pop from end
func (q *InnoDeque[T]) PopEnd() bool {
	if q.IsEmpty() {
		return false
	} else if q.front == q.end {
		q.front = nil
		q.end = nil
	} else {
		q.end = q.end.prev
		q.end.next = nil
	}
	q.size -= 1
	return true
}

// Ge size
func (q *InnoDeque[T]) Size() int {
	return q.size
}

// Insert at target index
func (q *InnoDeque[T]) Insert(val T, index int) {
	if q.IsEmpty() || index == 0 {
		q.PushFront(val)
	} else if index >= q.size {
		q.PushEnd(val)
	} else {
		node := q.front
		for i := 0; i < index; i++ {
			node = node.next
		}
		t := InnoDequeNode[T]{
			val:  val,
			prev: node,
			next: node.next,
		}
		node.next = &t
		t.next.prev = &t
	}
	q.size += 1
}

// Get index of element
func (q *InnoDeque[T]) IndexOf(val T) int {
	node, ans := q.front, 0
	for node != nil && node.val != val {
		node = node.next
		ans += 1
	}
	if node == nil {
		return -1
	}
	return ans
}

// Convert to a slice
func (q *InnoDeque[T]) ToSlice() []T {
	ans := make([]T, q.size)
	index := 0
	node := q.front
	for node != nil {
		ans[index] = node.val
		node = node.next
		index += 1
	}
	return ans
}
