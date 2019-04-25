import math
import numpy as np
import pandas as pd
import multiprocessing as mp
import csv

''' Utils '''
def process_frame(df):
    return len(df)

''' Read in data '''
#df = pd.read_csv('../data/page_aug.csv', delimiter=',',error_bad_lines=False, encoding='latin-1')

df = pd.read_csv('../data/page_aug.csv', delimiter=',', encoding='iso-8859-1', usecols=[0,1])
import pdb; pdb.set_trace()

''' Data preparation '''

