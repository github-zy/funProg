def factorial_r(x: int) -> int:
    if x == 0:
        return 1
    else:
        return x * factorial_r(x -1)
