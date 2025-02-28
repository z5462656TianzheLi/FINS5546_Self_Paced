def make_csv_name(tic,show = True):
    tic = tic.lower()
    tic_base = tic.split('.')
    csv_name = '{}_stock_price.csv'.format(tic_base[0])
    if show is True:
        print(csv_name)
    return csv_name

csv_name = make_csv_name('AAPL',True)