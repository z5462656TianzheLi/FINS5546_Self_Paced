""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

if __name__ == '__main__':

    import Lecture_4_4_Toolkit_Config as tkt_cfg
    import os

    #tic = 'NVDA'
    #datadir = r'C:\Users\samle\PycharmProjects\FINS5546_Self_Paced\data'

    # for AU stocks use this:
    #tic_base = tic.split('.')[0].lower()

    # for US stocks use this:
    #tic_base = tic.lower()

    #pth = r'{}\{}_stock_price.csv'.format(datadir,tic_base)
    #pth = os.path.join(datadir, tic_base + '_stock_price.csv')
    #print(pth)
    #yf_prc_to_csv(tic, pth)
    #print('Done')

    tic = 'NVDA'
    tic_base = tic.lower()
    pth = os.path.join(tkt_cfg.DATADIR, tic_base + '_stock_price.csv')
    yf_prc_to_csv(tic, pth)