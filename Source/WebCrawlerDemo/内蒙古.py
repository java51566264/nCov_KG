import requests
import time
from bs4 import BeautifulSoup
import re

class getContents():
    # 获取html页面
    def getHTMLText(self, url):
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""
    # 获取标题
    def getTitle(self, str):
        try:
            pat = re.compile(r'\d{4}-\d{2}-\d{2}')
            time = re.findall(pat, str)
            print(time)
            tag = BeautifulSoup(str, 'html.parser')
            title = tag.title.string
            return time[0] + " " + title
        except:
            return ""
    # 获取内容
    def getContent(self, str):
        try:
            soup = BeautifulSoup(str, 'html.parser')
            p = soup.find_all('span')
            if p.__len__() == 0:
                p = soup.find_all('font')
                if len(p) == 0:
                    p = soup.find_all('div')
            print(len(p))
            s = ""
            for i in p:
                if i.string == None:
                    continue
                s = s + i.text
            # print(s)
            return s
        except:
            return "1"
    # 写入内容
    def write(self, str, filename):
        try:
            filename = filename + '.txt'
            with open(filename, "w", encoding="utf-8") as f:
                f.write(str)
                print("成功")
        except:
            print("错误")


def main():
    with open("urlneimenggu.txt", 'r', encoding="utf-8") as f:
        url = f.read().split('\n')
        address = getContents()
        for i in url:
            # print(i)
            html = address.getHTMLText(i)
            while(True):
                if html == "":
                    print("等待中....")
                    time.sleep(5)
                    html = address.getHTMLText(i)
                else:
                    break
            title = address.getTitle(html)
            print(title)
            content = address.getContent(html)
            address.write(content, title)

main()