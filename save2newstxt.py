import requests as re
from bs4 import BeautifulSoup as BS
import pymysql


def savecuc(title, url):

    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'cucnews')
    cursor = db.cursor()

    sql = "insert into cucnewstxt(title,newsurl) values('%s','%s')" % (title, url)
    # sql='insert into cucnews(title,newsurl) values("中传要闻","cuc.edu.cn")'
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def savenewstxt(title,url,department,newsdate,count,content):
    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'cucnews')
    cursor = db.cursor()
    sql="select * from cucnewstxt where title='%s' and newsurl='%s'" %(title,newsurl)
    rs=cursor.execute(sql)
    if (not rs):
        sql = "insert into cucnewstxt(title,newsurl,department,newsdate,count,content) values('%s','%s','%s','%s','%s','%s')" % (title, url,department,newsdate,count,content)
        #sql='insert into cucnewstxt(title,newsurl,department,count,newsdate,content) values("中传要闻","cuc.edu.cn","计算机学院",100,"2019-04-14","赢了")'
        #sql = "insert into cucnewstxt(title,newsurl,department,newsdate,count,content) values('title','url','department','2019-04-12',100,'content')"

        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("can't save to mysql")
            db.rollback()
    db.close()


for i in range(1,425):
    url='http://by.cuc.edu.cn/zcyw/'+str(i)
    r=re.get(url,timeout=None)
    soup=BS(r.text,'html.parser')
    title=soup.find_all('h3',attrs={'class','tit'})
    for t in title:
        newsurl=t.find_all('a')
        urllen=str(newsurl[0]).find('target')
        newsurl=str(newsurl[0])[9:urllen-2]
        newstitle=t.get_text()
        print(newsurl)
        print(newstitle)
        #savecuc(newstitle,newsurl)
        #savenewstxt("title", "url", "department", "2019-04-12", 100, "content")

        j = 0
        while j <30:
            try:
                r = re.get(newsurl, timeout=5)
                j = 99
            except re.exceptions.RequestException:
                j += 1
        if(newsurl.__contains__("cuc.edu.cn")):
            soup = BS(r.text, 'html.parser')
            info = soup.find('sapn').get_text()
            print(info.find('来源：') + 7)
            print(info.find('20'))
            department=info[(info.find('来源：')+7):(info.find('20'))].strip()

            print(department)
            date=info[(info.find('20')):(info.find('20'))+10]
            print(date)
            countstr= soup.find('span', id='hits').get_text()
            #print(countstr)
            count=countstr.replace(",","")
            print(count)
            content=soup.find('article',attrs={'class', 'con-area'}).get_text()
            savenewstxt(newstitle,newsurl, department, date, count, content)
        else:
            savecuc(newstitle, newsurl)




