# report.py
import csv


def portfolio_dict(file_portfolio):
    

    portfolio = []
    with open(file_portfolio, 'r') as csvfile:
        lines = csv.reader(csvfile)
        next(lines)
    
        for line in lines:
            stock = {
                 'name'   : line[0],
                 'shares' : int(line[1]),
                 'price'   : float(line[2])
            }
            portfolio.append(stock)

    return portfolio

def prices_dict(file_price):
    prices = {}
    with open(file_price, 'r') as csvfile:
        lines = csv.reader(csvfile)

        for line in lines:
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                pass

    return prices


file_portfolio = '/Users/OLIZ/practical-python/Work/portfolio.csv'
file_price = '/Users/OLIZ/practical-python/Work/prices.csv'

portfolio = portfolio_dict(file_portfolio)
prices = prices_dict(file_price)

# Calculate the total cost of the portfolio
overal_cost = 0.0
for share in portfolio:
    overal_cost += share['shares']*share['price']

print('Original cost of shares', overal_cost)

# Compute the current value of the portfolio
overal_value = 0.0
for share in portfolio:
    overal_value += share['shares']*prices[share['name']]

print('Current cost of shares', overal_value)
print('Gain or Loss', overal_value - overal_cost)
