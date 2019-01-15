# coding=utf-8

import pandas as pd

def main():
    df = pd.read_csv('./data.csv', header=None, skiprows=1, nrows=1) 
    print len(df.values)

main()