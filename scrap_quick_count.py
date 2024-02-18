import time 
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

#PILEG
url = "https://www.cnnindonesia.com/pemilu2024/pileg-quickcount#"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)

all_lembaga = driver.find_element(By.CLASS_NAME, 'qc-content-tab.font-heading')
lembaga_a = all_lembaga.find_elements(By.TAG_NAME, 'a')

for lembaga in lembaga_a[0:2]:
    lembaga.click()
    time.sleep(5)

    zona = driver.find_element(By.CLASS_NAME, 'qc-graph__select')
    all_zona = zona.find_elements(By.TAG_NAME, 'option')

    data_dict = {'province':[],
                'info':[]}

    for zon in all_zona:
        zon.click()
        time.sleep(8)
        
        province = zon.text
        partai = driver.find_element(By.CLASS_NAME, 'qc-graph__list.font-heading')
        all_partai = partai.find_elements(By.TAG_NAME, 'li')

        info = driver.find_element(By.CLASS_NAME, 'qc-info.font-heading')
        time.sleep(10)

        for part in all_partai:
            all_value = part.text.split('\n')
            nama_partai = all_value[0]
            
            if nama_partai not in data_dict:
                data_dict[nama_partai] = [all_value[1]]
            else:
                data_dict[nama_partai].append(all_value[1])
        
        data_dict['info'].append(info.text.split('\n'))
        data_dict['province'].append(province)
        
        time.sleep(10)

data_pilkada_pileg = pd.DataFrame.from_dict(data_dict, orient="index").T

#pilpres
url = "https://www.cnnindonesia.com/pemilu2024/pilpres-quickcount"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)

all_lembaga = driver.find_element(By.CLASS_NAME, 'qc-content-tab.font-heading')
lembaga_a = all_lembaga.find_elements(By.TAG_NAME, 'a')

for lembaga in lembaga_a[2:3]:
    lembaga.click()
    time.sleep(5)

zona = driver.find_element(By.CLASS_NAME, 'qc-graph__select')
all_zona = zona.find_elements(By.TAG_NAME, 'option')

data_dict = {'paslon':[],
             'province':[],
             'info':[]}

for zon in all_zona:
    zon.click()
    time.sleep(8)
    
    province = zon.text
    all_info = driver.find_element(By.CLASS_NAME, 'qc-pilpresgraph__graph')
    all_paslon = all_info.find_elements(By.CLASS_NAME, 'qc-pilpresgraph__graph-paslon')
    info = driver.find_element(By.CLASS_NAME, 'qc-info.font-heading')

    for paslon in all_paslon:
        nama = paslon.find_element(By.CLASS_NAME, 'qc-pilpresgraph__graph-name').text
        value = paslon.find_element(By.CLASS_NAME, 'qc-pilpresgraph__graph-value').text

        data_dict['paslon'].append(f"{nama} {value}")
        data_dict['province'].append(province)
        data_dict['info'].append(info.text.split('\n'))

    time.sleep(10)

data_pilkada_pileg = pd.DataFrame.from_dict(data_dict, orient="index").T