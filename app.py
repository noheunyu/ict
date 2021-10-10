from flask import Flask, render_template,request
import pymysql
import time

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/iot', methods=["GET","POST"])
def iot():
    if request.method == 'GET':
        pir = request.args.get('pir')
        indate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        dbconn = pymysql.connect(
            host = 'noheunyu.mysql.pythonanywhere-services.com',
            port = 3306,
            user = 'noheunyu',
            passwd = 'ictdiffuser',
            db = 'ict',
            charset = 'utf8'
        )
        cursor = dbconn.cursor()
        sql = "insert into iot set pir = '%s', indate='%s';" % (pir,indate)
        cursor.execute(sql)
        dbconn.commit()
    return "ok"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)