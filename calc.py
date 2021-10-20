'''
app: compund interest calculator
function: calculates monthly compund interest for custom user inputs
author: matt

'''


def monthly_compounding(initial, monthly, years, annual_rate):
    sum = initial
    months = years * 12
    # iterate through months
    for month in range(int(months)):
        # apply annual rate to current balance
        sum = sum * (1 + annual_rate/1200)
        # add monthly contribution
        sum = sum + monthly
    return sum



