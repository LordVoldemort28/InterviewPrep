from math import e, log

def mySqrt(x):
    lo, hi = 0, x

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid * mid > x:
            hi = mid - 1
        elif mid * mid < x:
            lo = mid + 1
        else:
            return mid

    # When there is no perfect square, hi is the the value on the left
    # of where it would have been (rounding down). If we were rounding up,
    # we would return lo
    return hi

"""
n^2 = x
n = x^(0.5)
"""
def mySqrt2(x: int) -> int:
    if(x < 2):
        return x
    n = (e**(0.5*log(x)))
    if(round(n)*round(n) > x):
        return int(n)
    else:
        return round(n)

print(mySqrt(100))
