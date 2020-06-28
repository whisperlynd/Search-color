import pymysql
from bs4 import BeautifulSoup as BS
import requests

def saverec(url,ntitle,nfrom,ndate,ncontent,ncount):    
    # pymysql.connect(数据库url,用户名,密码,数据库名 )
    db = pymysql.connect("localhost", "root", "luoyujia990210", "cuc", charset = 'utf8')
    cursor = db.cursor()

    #for d in data:
    
    cursor.execute("INSERT INTO cucnews2(id,newsurl,title,newsfrom,newsdate,contents,newscount) VALUES(%d,%s,%s,%s,%s,%s,%s)",(id,url, ntitle,nfrom,ndate,ncontent,ncount))

    print("ok")
    db.commit()
db.close()

for i in range(1,2):
    url='http://by.cuc.edu.cn/zcyw/'+str(i)
    r=requests.get(url)
    soup=BS(r.text,'html.parser')
    title=soup.find_all('h3',attrs={'class','tit'})
    for t in title:
        newsurl=t.find_all('a')
        urllen=str(newsurl[0]).find('target')
        urlnei=str(newsurl[0])[9:urllen-2]
        url=urlnei
        r=re.get(url)
        #http://www.cuc.edu.cn/zcyw/246.html
        #http://www.cuc.edu.cn/zcyw/12521.html
        url=url.replace("http://www.cuc.edu.cn/zcyw/",'').replace(".html",'')
        print(url)
        id=int(url)
        soup = BS(r.text,'html.parser')
        title=soup.find_all('h1')
        newsfrom=soup.find_all('sapn')
        newsdate=soup.find_all('sapn')
        viewcount=soup.find_all('span',attrs={'id':'hits'})
        newscontent=soup.find_all('article',attrs={'class','con-area'})
        if title!=[]:
            ntitle=title[0].get_text()
            nfrom=''
            i=1
            while newsfrom[0].get_text()[26+i:27+i]!='\n':
                nfrom+=newsfrom[0].get_text()[26+i:27+i]
                i=i+1   

            print(nfrom)
            print(i-2)

            ndate=newsdate[0].get_text()[67+i-5:77+i-5]
            print(ndate)
            ncount=(viewcount[0].get_text())
            ncontent=newscontent[0].get_text()
