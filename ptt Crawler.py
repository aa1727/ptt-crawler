#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve 
import os

def img(art):
     for ar in art:
        print('https://www.ptt.cc'+ar['href'],ar.text)
        if not os.path.isdir(os.path.join('download',ar.text)):
            os.mkdir(os.path.join('download',ar.text))
        res = requests.get('https://www.ptt.cc'+ar['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print (ID)
            urlretrieve(image,os.path.join('download',ar.text,ID))
            
            
def crawler():
    if not os.path.isdir('download'):
        os.mkdir('download')
    url = "https://www.ptt.cc/bbs/PC_Shopping/index.html"
    for count in range(3):
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        name = 'div.title a'
        art = soup.select(name)
        #for ar in art:
            #print('https://www.ptt.cc'+ar['href'],ar.text)
        paging=soup.select('div.btn-group-paging a')
        next_url = "https://www.ptt.cc"+paging[1]['href']
        url = next_url
        img(art)
        
reg_imgur_file  = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
crawler()


# In[ ]:





# In[ ]:





# In[ ]:




