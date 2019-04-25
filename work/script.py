import numpy as np
import pandas as pd

''' Utils '''
def process_frame(df):
    return len(df)

''' Read in data '''
file_path = 'data_fixed/page_dec_fixed.csv'
df = pd.read_csv(file_path, delimiter=',', encoding='iso-8859-1')
import pdb; pdb.set_trace()

''' Data preparation '''

