name = "pywikiscraper"
import requests
from lxml import html
import re

class scrape:
    tree = 0
    head= []
    index =[]
    index_dict ={}
    text_dict = {}
    def httprequest(self,url):
        r = requests.get(url,verify=False)
        return html.fromstring(r.content)
    
    def headings(self,data):
        _data = []
        heading = data.xpath('//li[contains(@class, "toclevel-")]')
        for li in heading:
            text = str(li.xpath('./a/span[2]/text()')).strip("[]")[1:-1]
            no = str(li.xpath('./a/span[1]/text()')).strip("[]")[1:-1]    
            link = str(li.xpath('./a/@href')).strip("[]")[1:-1]
            _data.append([no,text,link])
            self.head.append([no,text])
        return _data
    
    def get_text(self,index):
        text_dict ={}
        for i in index:
            text_dict[i[0]]=self.get_tex_byeleid(i[2][1:])
        return text_dict
    
    def get_tex_byeleid(self,eid):
        lis = []
        x = self.tree.xpath('//*[@id="{0}"]/../following-sibling::*'.format(eid))
        for i in x:
            if i.tag == 'h2' or i.tag =='h3' or i.tag=='h4':
                return lis
            lis.append(i.text_content())
        return lis
    
    def indexdict(self,index):
        index_dict={}
        for i in index:
            index_dict[i[1]]=i[0]
        return index_dict
    
    def find_by_name(self,name):
        index = self.get_index_byname(name)
        if index=='':
            return 'No such heading available, use class.head to get the heading list'
        return self.text_dict[index]
    
    def find_by_key(self,num):
        if num in self.text_dict.keys():
            return self.text_dict[num]
        return 'Key not present in headings, use class.head to get the keys. PS -This takes a string as input not integer or float'
    
    def get_index_byname(self,name):
        result = ''
        for i in self.index:
            if i[1] == name:
                result = i[0]
        return result
    
    def __init__(self,url,printing=True):
        self.tree = self.httprequest(url)
        self.index = self.headings(self.tree)
        self.index_dict = self.indexdict(self.index)
        self.text_dict = self.get_text(self.index)
        if printing:
            print(self.head)
        