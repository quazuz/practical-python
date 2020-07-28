# fileparse.py
import csv

def parse_dict(file_portfolio, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    portfolio = []
    with open(file_portfolio) as csvfile:
        rows = csv.reader(csvfile, delimiter=delimiter)

        # Reading the file headers 
        headers = next(rows) if has_headers else []


        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for lineno, line in enumerate(lines, 1):
            if not line:     
                continue

            if select:
                line = [line[index] for index in indices]

            
            if types:
                try:
                    line = [func(val) for func, val in zip(types, line)]
                except ValueError as err:
                    if not silence_errors:
                        print(f"Row {lineno}: Couldn't convert {line}")
                        print(f"Row {lineno}: Reason {err}")
                    continue

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, line))
            else:
                record = tuple(line)
            records.append(record)

        return records
file_portfolio = '/Users/OLIZ/practical-python/Work/Data/missing.csv'
portfolio = parse_dict(file_portfolio)