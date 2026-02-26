def countdown(n):
    """
    Docstring for countdown()
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:        # base case
        print(0)
    else:
        print(n)
        countdown(n - 1)

def sum_to_zero(k):
    """
    Docstring for sum_to_zero
    """
    if k < 0:
        raise ValueError("k must be non-negative")

    if k == 0:
        return 0
    else:
        return k + sum_to_zero(k - 1)
    

def factorial(n):
    """
    Docstring for factorial()
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)