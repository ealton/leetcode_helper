def getOverlappingArea(
    r1xLow: int,
    r1xHigh: int,
    r1yLow: int,
    r1yHigh: int,
    r2xLow: int,
    r2xHigh: int,
    r2yLow: int,
    r2yHigh: int,
) -> int:
    xLow = max(r1xLow, r2xLow)
    xHigh = min(r1xHigh, r2xHigh)
    yLow = max(r1yLow, r2yLow)
    yHigh = min(r1yHigh, r2yHigh)

    x = max(xHigh - xLow, 0)
    y = max(yHigh - yLow, 0)

    return x * y
