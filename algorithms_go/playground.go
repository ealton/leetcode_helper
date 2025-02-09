package algorithmsgo

import (
	"container/heap"
	"strconv"
	"strings"
)

func minimizeXor(num1 int, num2 int) int {
    num1Bin := strings.Split(strconv.FormatInt(int64(num1), 2), "")
    num1Bits := 0
    for _, item := range num1Bin {
        if item == "1" {
            num1Bits++
        }
    }
    num2Bin := strings.Split(strconv.FormatInt(int64(num2), 2), "")
    num2Bits := 0
    for _, item := range num2Bin {
        if item == "1" {
            num2Bits++
        }
    }

    if num1Bits == num2Bits {
        return num1
    }
    if num1Bits > num2Bits {
        for i, item := range num1Bin {
            if num2Bits == 0 {
                break
            }
            if item == "1" {
                num2Bits--
            } else {
                num1Bin[i] = "0"
            }
        }
        ans, _ := strconv.ParseInt(strings.Join(num1Bin, ""), 2, 64)
        return int(ans)
    } 
    
    // num2Bits > num1Bits
    n := len(num1Bin)
    for i:=0; i<n/2; i++ {
        num1Bin[i], num1Bin[n-1-i] = num1Bin[n-1-i], num1Bin[i]
    }
    num2Bits -= num1Bits
    for i, item := range num1Bin {
        if num2Bits == 0 {
            break
        }
        if item == "1" {
            continue
        } else {
            num1Bin[i] = "1"
            num2Bits--
        }
    }
    for i:=0; i<num2Bits; i++ {
        num1Bin = append(num1Bin, "1")
    }
    n = len(num1Bin)
    for i:=0; i<n/2; i++ {
        num1Bin[i], num1Bin[n-1-i] = num1Bin[n-1-i], num1Bin[i]
    }
    ans, _ := strconv.ParseInt(strings.Join(num1Bin, ""), 2, 64)
    return int(ans)
}



func leftmostBuildingQueries(heights []int, queries [][]int) []int {
	mHeap := &CustomHeap{}
    storeQueries := make([][][]int, len(heights))

    ans := make([]int, len(queries))
    for i:=0; i<len(queries); i++ {
        ans[i] = -1
    }

    for i, item := range queries {
        p1, p2 := item[0], item[1]
        if p1 == p2 {
            ans[i] = p1
        } else if p1 > p2 && heights[p1] > heights[p2] {
            ans[i] = p1
        } else if p2 > p1 && heights[p2] > heights[p1] {
            ans[i] = p2
        } else {
            targetIndex := max(p1, p2)
            targetValue := max(heights[p1], heights[p2])
            storeQueries[targetIndex] = append(storeQueries[targetIndex], []int{targetValue, i})
        }
    }

    for i, height := range heights {
        for mHeap.Len() > 0 && mHeap.Peek().([]int)[0] < height {
            item := heap.Pop(mHeap).([]int)
            ans[item[1]] = i
        }

        for _, item := range storeQueries[i] {
            heap.Push(mHeap, item)
        }
    }

    return ans
}

type CustomHeap [][]int

// Len implements heap.Interface.
func (c CustomHeap) Len() int { return len(c) }

// Less implements heap.Interface.
func (c CustomHeap) Less(i int, j int) bool { return c[i][0] < c[j][0] }

// Pop implements heap.Interface.
func (c *CustomHeap) Pop() any {
    temp := *c
    x := temp[len(temp)-1]
    *c = temp[:len(temp)-1]
    return x
}

func (c *CustomHeap) Peek() any {
    return (*c)[0]
}

// Push implements heap.Interface.
func (c *CustomHeap) Push(x any) {
    *c = append(*c, x.([]int))
}

// Swap implements heap.Interface.
func (c CustomHeap) Swap(i int, j int) {
    c[i], c[j] = c[j], c[i]
}
