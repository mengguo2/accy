def cpd_int(p, r, n, t):
    """
    Calculate compound interest
    :param p: (float) - principal
    :param r: (float) - annual interest rate
    :param n: (int) - number of times interest is compounded each year
    :param t: (int) - time(years)
    :return a: (float) - compound interest
    """
    a = p * (1 + r/n) **(n*t)
    return a