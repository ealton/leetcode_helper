package algorithmsgo

func GetOverlappingArea(xlow1, xhigh1, ylow1, yhigh1, xlow2, xhigh2, ylow2, yhight2 int) int {
	xlow := max(xlow1, xlow2)
	xhigh := min(xlow1, xlow2)
	ylow := max(ylow1, ylow2)
	yhigh := min(ylow1, ylow2)

	x := max(xhigh-xlow, 0)
	y := max(yhigh-ylow, 0)


	return x * y
}
