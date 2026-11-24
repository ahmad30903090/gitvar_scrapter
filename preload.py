import threading
import time
from threading import Thread
import json
import httpx
from debugpy.server.cli import switches
from pyparsing import unicode
import re
import VillaProperty
import requests as rq
from bs4 import BeautifulSoup

def gitvar_preload():
    url="https://divar.ir/s/najafabad/buy-villa"
    r=rq.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup.original_encoding
    'utf-8'
    obj1 = soup.find_all('script', type='application/ld+json')
    aproch=""
    if len(obj1)>1:
        aproch =str(obj1[len(obj1)-1].string)
        aproch1=obj1[len(obj1)-1].get_text().strip()
        print("aproch 1 is ",aproch1)
    mytext="\u200c"
    myjson=json.loads(aproch)
    Errore_List=list()
    tead=0
    for item in myjson:
        print("list number ",tead)
        print(item['url'])
        url=url+"?tracker_session_id=154ba964-0c37-4f71-be36-d7e0b7598a84_ga4VqpFO_N"
        time.sleep(10)
        #url_thread=threading.Thread(target=(scrapt_with_url(item['url'],)))
        #url_thread = threading.Thread(target=(scrapt_with_url("https://divar.ir/v/%D8%A2%D9%87%D9%86-%D8%A2%D8%AC%D8%B1-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%B4%D8%B1%D9%82-%D9%86%D8%AC%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF/gaw9ka7f", )))
        #url_thread.start()
        #url_thread.join()
        #scrapt_with_url("https://divar.ir/v/%D8%A2%D9%87%D9%86-%D8%A2%D8%AC%D8%B1-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%B4%D8%B1%D9%82-%D9%86%D8%AC%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF/gaw9ka7f")
        #break
        if tead%2==1:
            time.sleep(3)
        else:
            time.sleep(7)
        if tead ==9:
            break
        tead+=1

    if len(Errore_List)>0:
        for item in Errore_List:
            print(item)
            time.sleep(10)
            #url_thread = threading.Thread(target=(scrapt_with_url(item, )))
            # url_thread = threading.Thread(target=(scrapt_with_url("https://divar.ir/v/%D8%A2%D9%87%D9%86-%D8%A2%D8%AC%D8%B1-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%B4%D8%B1%D9%82-%D9%86%D8%AC%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF/gaw9ka7f", )))
            #url_thread.start()
            #url_thread.join()
            time.sleep(10)
    #from lxml.html.clean import unicode