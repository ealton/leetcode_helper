package algorithmsgo

import (
	"fmt"
	"reflect"
	"testing"
)

func TestDequeue(t *testing.T) {
	fmt.Println("Starting TestDequeue")
	q := InitInnoDeque[int]()
	q.PushFront(1)
	q.PushFront(2)
	assert(t, q.IndexOf(2), 0)
	assert(t, q.IndexOf(1), 1)
	assert(t, q.IndexOf(0), -1)
	assert(t, q.Size(), 2)
	q.PushEnd(4)
	q.PushEnd(5)
	assert(t, reflect.DeepEqual(q.ToSlice(), []int{2, 1, 4, 5}), true)
	assert(t, q.Size(), 4)
	assert(t, q.PopFront(), true)
	assert(t, q.PopFront(), true)
	assert(t, q.PopEnd(), true)
	assert(t, q.PopFront(), true)
	assert(t, q.PopFront(), false)

	q2 := InitInnoDeque[string]()
	q2.PushFront("1")
	q2.PushFront("2")
	assert(t, q2.IndexOf("2"), 0)
	assert(t, q2.IndexOf("1"), 1)
	assert(t, q2.IndexOf("0"), -1)
	assert(t, q2.Size(), 2)
	q2.PushEnd("4")
	q2.PushEnd("5")
	assert(t, reflect.DeepEqual(q2.ToSlice(), []string{"2", "1", "4", "5"}), true)
	assert(t, q2.Size(), 4)
	assert(t, q2.PopFront(), true)
	assert(t, q2.PopFront(), true)
	assert(t, q2.PopEnd(), true)
	assert(t, q2.PopFront(), true)
	assert(t, q2.PopFront(), false)
}
