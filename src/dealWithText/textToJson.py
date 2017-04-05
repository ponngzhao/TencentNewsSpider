#coding:utf-8
import pymysql
import re
from bs4 import BeautifulSoup

#连接数据库
db = pymysql.connect("localhost","root","stone","tencent_news")
cursor = db.cursor()

#从url_info中得到json_number
def getJsonNumber():
    sql = "SELECT json_number FROM url_info;"
    cursor.execute(sql)
    resultes = cursor.fetchall()
    jsonNumber = resultes[0][0]
    return jsonNumber

#根据json_number得到pageText
def getPageText(jsonNumber):
    f = open("./pageText/"+str(jsonNumber)+".htm","r")
    # f.decode("gb2312")
    pageText = f.read()
    f.close()
    return pageText

#根据pageText得到charset
def getCharset(pageText):
    charset = re.findall("<meta charset=\"(.*?)\">",pageText)
    charset = charset[0]
    return charset

#根据pageText得到title
def getTitle(pageText):
    soup = BeautifulSoup(pageText,"lxml")
    title = soup.h1.string
    return title

#根据pageText得到新闻类型
def getType(pageText):
    soup = BeautifulSoup(pageText,"lxml")
    print(soup.find(accesskey="5"))
    
def main():
    jsonNumber = 1
    pageText = getPageText(jsonNumber)
    title = getTitle(pageText)
    charset = getCharset(pageText)
    getType(pageText)
    # print(charset)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))