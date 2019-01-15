# coding=utf-8

import pandas as pd

def main():
    df = pd.read_csv('./data.csv', header=None) 
    print df.values[0][0]

main()