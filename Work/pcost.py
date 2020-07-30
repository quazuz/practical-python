# pcost.py
import csv
def portfolio_cost(file_portfolio):
   
    total_cost = 0.0
    portfolio_cost = []
    with open(file_portfolio) as csvfile:
        lines = csv.reader(csvfile)
        headers = next(lines)
        for lineno, list in enumerate(lines, start=1):
            record = dict(zip(headers, list))
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                total_cost = total_cost + num_shares * price
            
            except ValueError:
                print(f'List {lineno}: Bad list: {line}')

    return total_cost
file_portfolio = '/Users/OLIZ/practical-python/Work/Dataportfoliodate.csv'
portfolio = portfolio_cost(file_portfolio)
import sys
if len(sys.argv) == 2:
    file_portfolio = sys.argv[1]
else:
    file_portfolio = input('Enter a filename:')

cost = portfolio_cost(file_portfolio)
print('Total cost:', cost)

# Exercise 1.27
