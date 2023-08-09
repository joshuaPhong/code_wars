def is_square(n):
    if n == 0:  # 0 is a square
        return True
    elif n > 0:  # no negative numbers
        for i in range(1, n + 1):
            if n % i == 0:
                if i ** 2 == n:
                    return True
    return False


def is_square_optimised(n):
    if n == 0:
        return True
    if n < 0:
        return False
    sqr_n = int(n ** 0.5)
    if (sqr_n * sqr_n) == n:
        return True
    else:
        return False


print(is_square_optimised(787904570))
