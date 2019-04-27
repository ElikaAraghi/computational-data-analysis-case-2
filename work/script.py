import numpy as np
import pandas as pd
from langdetect import detect

''' Utils '''
def get_page_title_languages(titles):
    lang_title_dict = {}
    count=0
    import pdb; pdb.set_trace()
    print('Getting languages...')
    for title in titles:
        try:
            detected_title_lang = detect(title)
            if detected_title_lang in titles:
                lang_title_dict[detected_title_lang].append(title)
            else:
                lang_title_dict[detected_title_lang] = [title]
        except:
            lang_title_dict[title] = 'bad language'
        if count % 10 == 0:
            print("Progress: {0} languages detected".format(count))
        count = count + 1
    print('Languages detected...')
    return lang_title_dict

''' Read in data '''
file_path = '../../data_fixed/page_aug_fixed.csv'
df = pd.read_csv(file_path, delimiter=',', encoding='iso-8859-1')

''' Data preparation '''
data = df[['sessionnumber', 'pagetitle', 'eventtimestamp']]
data = data.drop([8621281,8621282])
data.eventtimestamp = data.eventtimestamp.astype(int)
data = data.sort_values(by='eventtimestamp')

session_dict = {}
counter = 0
import pdb; pdb.set_trace()
for _, row in data.iterrows():
    session_number = row.sessionnumber
    page_title = row.pagetitle
    if session_number in session_dict:
        session_dict[session_number].append(page_title)
    else:
        session_dict[session_number] = [page_title]

    if counter % 1000 == 0:
        print('Progress: processed {0} session numbers'.format(counter))
    counter = counter + 1
import pdb; pdb.set_trace()

