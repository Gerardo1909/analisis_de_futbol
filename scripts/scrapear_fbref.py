'''
    script hecho para el scrapeo de fbref
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import time


def _obtener_tabla(soup):
    return soup.find_all('table')[0]

def _parsear_fila(row):
    cols = None
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    return cols

def obtener_df_jugadores(path):
    URL = path
    time.sleep(4)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    comment = soup.find_all(text=lambda t: isinstance(t, Comment))
    c=0
    for i in range(len(comment)):
        if comment[i].find('\n\n<div class="table_container"') != -1:
            c = i
    a = comment[c]
    tbody = a.find('table')
    sp = BeautifulSoup(a[tbody:], 'html.parser')
    table = _obtener_tabla(sp)
    data = []
    headings=[]
    headtext = sp.find_all("th",scope="col")
    for i in range(len(headtext)):
        heading = headtext[i].get_text()
        headings.append(heading)
    headings=headings[1:len(headings)]
    data.append(headings)
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row_index in range(len(rows)):
        row = rows[row_index]
        cols = _parsear_fila(row)
        data.append(cols)

    data = pd.DataFrame(data)
    data = data.rename(columns=data.iloc[0])
    data = data.reindex(data.index.drop(0))
    data = data.replace('',0)
    return data