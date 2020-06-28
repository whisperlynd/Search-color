import requests as re
from bs4 import BeautifulSoup as BS
import pymysql


def savecuc(title, url):

    db = pymysql.connect('localhost', 'root', 'luoyujia990210', 'cucnews')
    cursor = db.cursor()

    sql = "insert into cucnews(title,newsurl) values('%s','%s')" % (title, url)
    # sql='insert into cucnews(title,newsurl) values("中传要闻","cuc.edu.cn")'
    #try:
    cursor.execute(sql)
    db.commit()
# except:
#	db.rollback()
#    db.close()

#try:
for i in range(1,425):
	url='http://by.cuc.edu.cn/zcyw/'+str(i)
	r=re.get(url)
	soup=BS(r.text,'html.parser')
	title=soup.find_all('h3',attrs={'class','tit'})
	for t in title:
		newsurl=t.find_all('a')
		urllen=str(newsurl[0]).find('target')
		newsurl=str(newsurl[0])[9:urllen-2]
		newstitle=t.get_text()
		#print(newsurl)
		#print(newstitle)
		savecuc(newstitle,newsurl)
#except:
#    print("Error")


