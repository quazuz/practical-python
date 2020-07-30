#report_2_11


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



def make_report(a,b):
    lines = []
    for stock in a:
        cur_price = b[stock['name']]
        difference = cur_price - stock['price']
        report_sum = (stock['name'],stock['shares'],"${:,.2f}".format(cur_price), difference)
        lines.append(report_sum)
    return lines


file_portfolio = '/Users/OLIZ/practical-python/Work/portfolio.csv'
file_price = '/Users/OLIZ/practical-python/Work/prices.csv'
portfolio = portfolio_dict(file_portfolio)
prices = prices_dict(file_price)


report = make_report(portfolio,prices)
#for r in report:
    #print(r)




headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' %headers)
print(('-' * 10 + ' ') * len(headers))
for line in report:
    print('%10s %10d %10s %10.2f' % line)


#Exercise 2.12





