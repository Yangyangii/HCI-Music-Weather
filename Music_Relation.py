# -*- coding: utf-8 -*-


import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys


# In[2]:

weathers = pd.read_csv('./data/wunder_data.csv', encoding='utf-8-sig')
mania_musics = pd.read_csv('./data/mania_enco.csv', encoding='utf-8-sig')
all_chart_musics = pd.read_csv('./data/bugs_data.csv', encoding='utf-8-sig')


# In[3]:

mania_musics.loc[:, 'cnt'] = pd.Series(np.ones(146626))
musics_for_title = mania_musics.copy()
musics_for_artist = mania_musics.copy()
mania_musics.head()


# In[4]:

del musics_for_title['Rank']
del musics_for_title['Date']
del musics_for_title['ID']
del musics_for_artist['Rank']
del musics_for_artist['Date']
del musics_for_artist['ID']


# In[5]:

#distinct_musics = mania_musics.drop_duplicates({'Title', 'Artist'})
#distinct_musics
g_musics_for_title = musics_for_title.groupby(['Title', 'Artist'])
cnt_for_title = g_musics_for_title.sum().sort('cnt', ascending=False)
cnt_for_title


# In[6]:

g_musics_artist = musics_for_artist.groupby(['Artist'])
cnt_for_artist = g_musics_artist.sum().sort('cnt', ascending=False)
cnt_for_artist


# In[109]:

temp_artist = cnt_for_artist[cnt_for_artist['cnt'] > 100]
temp_title = cnt_for_title[cnt_for_title['cnt'] > 100]
matplotlib.rc('font', family='DejaVu Serif')
print temp_artist.count()
print temp_title.count()
temp_title
# matplotlib.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
#temp_artist.plot(kind='bar', color='g', alpha=0.7)


# In[30]:

temp_title.plot(kind='bar', color='g', alpha=0.7)

# In[88]:

target_year = [2011, 2012, 2013, 2014, 2015]
temp_y_musics = []
for i in range(len(target_year)):
    tf = mania_musics['Date'] // 10000 == target_year[i]
    temp_musics = mania_musics[tf].copy()
    del temp_musics['Rank']
    del temp_musics['Date']
    del temp_musics['ID']
    temp_musics = temp_musics.groupby(['Title', 'Artist'])
    temp_y_musics.append(temp_musics.sum().sort('cnt', ascending=False))
for i in range(5):
    print target_year[i], '년 10위권 ======'
    print temp_y_musics[i][:10]
    print '\n\n\n'
    
    


# In[92]:


temp_y_musics[1][:10]


# In[ ]:




# In[ ]:




# In[23]:

pd.version.short_version

