# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json


web_url = "https://www.nytimes.com/crosswords/game/mini"
def WebScrap(url):
    req = requests.get(url)
    source = BeautifulSoup(req.content,"html.parser")
        
    
    json_dict={"baslik":[],"Number":[],"String":[]}
    baslik,icerik_sayi,icerik=[],[],[]
    
        
    for i in source.find_all("h3",attrs={"class":"ClueList-title--1-3oW"}):
        baslik.append(i.text)
                    
    for i in source.find_all("span",attrs={"class":"Clue-label--2IdMY"}):
        icerik_sayi.append(i.text)        
        
        
    for i in source.find_all("span",attrs={"class":"Clue-text--3lZl7"}):
        icerik.append(i.text) 
        
        
        
    print("="*3,baslik[0],"="*3)
    for i in range(len(icerik)):
        if(i==5):
            print("="*3,baslik[1],"="*3)
        print(icerik_sayi[i],icerik[i])
      
    
        
    for z in range(5) :
        json_dict["Number"].append(icerik_sayi[z])
        json_dict["String"].append(icerik[z])
    
    json_dict["baslik"].append(baslik[0])              
             
                   
    with open('botjsn.json','w') as output:
        json.dump(json_dict, output)  
     
   
WebScrap(web_url)
