from accy.accy_functions import cpd_int
"""
A. If a 15-year-old student deposits $500 to an online savings account,
which offers a constant monthly interest rate of 1.6%, what would
his savings be by the time he is 30 years old, assuming he does not
add put in any extra money? 
"""
initial_dep = 500
interest_rate = 0.016
nyears = 30 - 15
total_savings = cpd_int(initial_dep, interest_rate, nyears)
print('A. The student would have ${0:.2f}!'.format(total_savings))

"""
B. What would the total amount be if the interest rate was halved to 0.8%? 
"""

"""
C. Again assuming the interest rate is 1.6%, how much money would have
accrued by the time he is 50 years old?
"""

"""
D. What if the student deposited the $500 when he was 20 instead of 15?
How much money would he have by the time he is 30 years old?
"""

"""
E. Again assuming the student starts depositing at 15 years old,
what is his total if he adds an extra 100$ every year until he is 30?
"""