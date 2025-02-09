package algorithmsgo

import (
	"fmt"
	"testing"
)

func TestIsPrime(t *testing.T) {
	fmt.Println("Starting TestIsPrime")

	assert(t, IsPrime(1), false)
	assert(t, IsPrime(2), true)
	assert(t, IsPrime(3), true)
	assert(t, IsPrime(4), false)
	assert(t, IsPrime(5), true)
	assert(t, IsPrime(6), false)
	assert(t, IsPrime(7), true)
	assert(t, IsPrime(8), false)
	assert(t, IsPrime(9), false)
	assert(t, IsPrime(10), false)
	assert(t, IsPrime(13), true)
	assert(t, IsPrime(15), false)
	assert(t, IsPrime(17), true)
	assert(t, IsPrime(101), true)
	assert(t, IsPrime(999), false)
	assert(t, IsPrime(1223), true)
}
