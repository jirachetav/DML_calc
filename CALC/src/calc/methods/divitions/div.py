def divide(left, right):
    """

    Args:
      left: valor que dividendo
      right: valor de divisor

    Returns: A/B

    """
    if right == 0:
        raise ValueError("Division by zero is not allowed")
    return left / right