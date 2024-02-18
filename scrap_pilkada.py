import requests
import pandas as pd
import re

from tqdm import tqdm
from bs4 import BeautifulSoup

link_data = pd.read_excel("link kabkot.xlsx")
link_data['new_link'] = link_data['link'].apply(lambda x: re.search(r'https://[^\s]+', x).group())

link_kabkot = link_data['new_link'].to_list()

link_not_found = []
link_found = []

#to split link fonud and not found in citys
for link in tqdm(link_kabkot, desc="Progress Split Link"):
    cek = re.search(r'https://[^\s]+&action=edit&redlink=1', link)
    
    if cek:
        link_not_found.append(cek.group())
    else:
        link_found.append(link)

data_dict = {'bakal_calon':[],
             'provinsi':[],
             'link_kabkot':[]}

#get data in link found
for url in tqdm(link_found, desc="Progress Get Data"):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    raw_data = soup.find('div',attrs={'id':'mw-content-text'})
    ul = raw_data.find('ul')
    provinsi = re.search(r'Pemilihan_umum_[^\s]+',url).group()

    if ul :
        for u in ul:
            data_dict['bakal_calon'].append(u)
            data_dict['provinsi'].append(provinsi)
            data_dict['link_kabkot'].append(url)
    else:
        data_dict['bakal_calon'].append(None)
        data_dict['provinsi'].append(provinsi)
        data_dict['link_kabkot'].append(url)

data_pilkada = pd.DataFrame.from_dict(data_dict, orient="index").T
data_pilkada = data_pilkada[data_pilkada['bakal_calon'] != '\n']
data_pilkada['bakal_calon'] = data_pilkada['bakal_calon'].astype(str)

data_pilkada.to_excel("asw.xlsx")