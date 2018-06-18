def cpd_int(p, r, t, n=12):
    """
    Calculate compound interest
    :param p: (float) - principal
    :param r: (float) - annual interest rate
    :param t: (int) - time(years)
    :param n: (int) - number of times interest is compounded each year
    :return a: (float) - compound interest
    """
    a = p * (1 + r / n) ** (n * t)
    return a
