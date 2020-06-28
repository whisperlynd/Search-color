from flask import Flask,render_template,redirect
import pymysql

app=Flask(__name__)
@app.route("/")
def index():
    #return render_template("index.html")
    return redirect("name/cucnewstxt")

@app.route("/name/<table>")
def select(table):
    db = pymysql.connect('localhost', 'root', '123456', 'engword')
    cursor = db.cursor()

    sql = "select  * from %s where count>5000 order by count desc "%table
    try:
        rscount=cursor.execute(sql)     #返回记录数
        rs=cursor.fetchall()
    except:
        print("Error")
    db.close()

    return render_template("select.html",count=rscount,rs=rs)

if __name__=="__main__":
    app.run(host='0.0.0.0',port="5001")