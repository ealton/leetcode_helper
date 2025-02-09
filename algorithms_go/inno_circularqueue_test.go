package algorithmsgo

import (
	"fmt"
	"testing"
)

func TestCircularQueue(t *testing.T) {
	fmt.Println("Starting TestCircularQueue")
	size := 3
	q := InitCircularQueue[int](size)
	assert(t, q.EnQueue(1), true)
	assert(t, q.EnQueue(2), true)
	assert(t, q.EnQueue(3), true)
	assert(t, q.EnQueue(4), false)
	assert(t, q.Rear(), 3)
	assert(t, q.IsFull(), true)
	assert(t, q.DeQueue(), true)
	assert(t, q.EnQueue(4), true)
	assert(t, q.Rear(), 4)

	q2 := InitCircularQueue[string](size)
	assert(t, q2.EnQueue("1"), true)
	assert(t, q2.EnQueue("2"), true)
	assert(t, q2.EnQueue("3"), true)
	assert(t, q2.EnQueue("4"), false)
	assert(t, q2.Rear(), "3")
	assert(t, q2.IsFull(), true)
	assert(t, q2.DeQueue(), true)
	assert(t, q2.EnQueue("4"), true)
	assert(t, q2.Rear(), "4")
}
