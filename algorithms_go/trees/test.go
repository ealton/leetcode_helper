package trees

import (
	"runtime/debug"
	"testing"
)

func assert(t *testing.T, actualResult any, expectedResult any) {
	if actualResult != expectedResult {
		t.Error(string(debug.Stack()))
		t.Error("Error")
	}
}

func assertNotEqual(t *testing.T, actualResult any, expectedResult any) {
	if actualResult == expectedResult {
		t.Error(string(debug.Stack()))
		t.Error("Error")
	}
}
