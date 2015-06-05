# -*- coding: utf-8 -*-

import requests
from lxml.html      import fromstring
import re

__author__ = 'Roman'

print("Парсер авито v0.01")


# авито #
_site_ = "https://m.avito.ru/"
_direc_ = "kaluga/kvartiry"


def parse_site():
    i = 1
    k = 0
    page = 1
    href = "/kaluga/kvartiry/2-k_kvartira_61_m_35_et._583514707"
    #while i < 1:
        #while k < 1:
    site = requests.get(_site_+_direc_+"?p=2")
    textS = fromstring(site.text)
    info_data = textS.cssselect('section.b-content-main')[0]
    temp = info_data.cssselect('article.b-item ')
    for elem in temp:
        print("++++++++  "+str(i)+"  ++++++++++")
        print(elem.text_content())
        i = i +1
        if len(temp)-2 == i:
            break

    print("Vsego:  " + str(i))
    page = page + 1



def main():
	parse_site()


if __name__ == '__main__':
	main()


