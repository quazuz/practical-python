# fileparse.py
import csv

def parse_dict(file_portfolio, select=None, types=None, has_headers=True, delimiter=','):
    potfolio = []
    with open(file_portfolio, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=delimiter)

        # Reading the file headers 
        headers = next(lines) if has_headers else []

        # If specific columns have been selected, make indices for filtering 
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for line in lines:
            if not line:     
                continue

            
            if select:
                line = [ line[index] for index in indices]

            if types:
                line = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, line))
            else:
                record = tuple(line)
            records.append(record)

        return records
file_portfolio = '/Users/OLIZ/practical-python/Work/Data/portfolio.dat'
portfolio = parse_dict(file_portfolio)