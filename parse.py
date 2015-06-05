# -*- coding: utf-8 -*-

import requests
from lxml.html      import fromstring
import re

__author__ = 'Roman'

print("Парсер авито v0.01")


# авито #
_site_ = "https://www.avito.ru/"
_direc_ = "kaluga/kvartiry"


def parse_site():
    i = 0
    k = 0
    page = 1
    id_last = ""
    #while i < 1:
        #while k < 1:
    site = requests.get(_site_+_direc_+"/prodam?p=1")
    textS = fromstring(site.text)
    info_data = textS.cssselect('div.catalog_table')[0]
    temp = info_data.cssselect('div.item_table')
    for elem in temp:
        i = i +1
        info = elem.cssselect('h3.title')[0]
        info_ob = info.text_content().strip()
        a =  info.cssselect("a")[0]
        href0=a.get('href')[17:]
        adress = elem.cssselect('p')[0].text_content().strip()
        agent = elem.cssselect('p')[1].text_content().strip()
        price_temp = elem.cssselect('div.about')[0].text_content().strip()
        rr = price_temp.find(".")
        price = price_temp[:rr-3]
        if agent == '':
            k = k+1
            print("++++++++  "+str(i)+"  ++++++++++")
            print(info_ob)
            print(href0)
            print(agent)
            print(adress)
            print(price)
            print("++++++++++++++++++++++++")
        if id_last == href0:
            break


    print("Vsego:  " + str(i))
    print("Частники:  " + str(k))
    page = page + 1



def main():
	parse_site()


if __name__ == '__main__':
	main()


