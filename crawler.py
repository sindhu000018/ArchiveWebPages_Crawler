import pandas as pd
from bs4 import BeautifulSoup
import requests
import json

df=pd.read_excel('Archival.xlsx')
org_links=df.iloc[:, 0] 
base_url='https://web.archive.org/save/'
archive_links=[]
for i in range(len(org_links)):
  input_url=org_links[i]
  url_save=base_url+input_url
  response = requests.get(url_save, headers={'User-Agent': 'Mozilla/5.0'})
  soup = BeautifulSoup(response.content, 'html.parser')
  IDlinks = []
  for link in soup.find_all('a'):
    IDlinks.append(link.get('href'))
  str_val_temp=IDlinks[0]
  str_val=str_val_temp.split('/')[2]
  archive_link='https://web.archive.org/web/'+str(str_val)+'/'+input_url
  archive_links.append(archive_link)
df['Archival Link']=archive_links
df.head()
df.to_csv('Archival.csv')
print("completed Archival")
