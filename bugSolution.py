def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1/x
        else:
            return x + 1
    except ZeroDivisionError:
        return float('inf')  # Handle the error gracefully, returning positive infinity