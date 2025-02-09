package algorithmsgo

import (
	"errors"
	"fmt"
	"testing"
)

func TestZAlgorithm(t *testing.T) {
	fmt.Println("Starting TestZAlgorithm")
	params := [][]any{
		{"abcd", "fdafewreabcddafwe", true},
		{"abcd", "fdafewreabdcafwe", false},
	}
	fmt.Println(BuildZList("abababab"))
	fmt.Println(BuildZList("ba.ababab"))
	for _, item := range params {
		needle, haystack, expected := item[0].(string), item[1].(string), item[2].(bool)
		zList := BuildZList(needle + "." + haystack)
		fmt.Println(zList)
		assert(t, SliceContains(len(needle), &zList), expected)
	}
	panic(errors.New(""))
}

func TestKmpAlgorithm(t *testing.T) {
	fmt.Println("Starting TestKmpAlgorithm")
	params := [][]any{
		{"abcd", "fdafewreabcddafwe", 8},
		{"abcd", "fdafewreabdcafwe", -1},
	}
	for _, item := range params {
		needle, haystack, expected := item[0].(string), item[1].(string), item[2].(int)
		result := KmpSearch(needle, haystack)
		assert(t, result, expected)
	}
}
