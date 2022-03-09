import requests
from bs4 import BeautifulSoup as bs
import json
import csv

def parc():
    headers={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36'
        }
    
    all_list=[]
    for i in range(1,9):
        
        ur=f'https://shop.casio.ru/catalog/?PAGEN_1={i}'
        req=requests.get(ur,headers=headers)
        src=req.content
        soup=bs(src,'lxml')
        item__link=soup.find_all(class_='product-item__link')
        item__articul=soup.find_all(class_='product-item__articul')
        item_price=soup.find_all(class_='product-item__price')
        
        for e,m,t in zip(item__articul,item_price,item__link):
            s='https://shop.casio.ru'+t.get('href')
            s=s.strip()
            e=e.text
            e=e.strip()
            m=m.text
            m=m.strip()
            all={
                'модель часов':e,
                'цена':m,
                'ссылка':s

            }

            all_list.append(all)
            
            with open('parc.csv','a',encoding='utf-8') as file:
                file_writer = csv.writer(file)
                file_writer.writerow((
                        e,
                        m,
                        s
                        ))
    with open('parc.json','a',encoding='utf-8') as file:
        json.dump(all_list,file,indent=4,ensure_ascii=False)    


parc()
