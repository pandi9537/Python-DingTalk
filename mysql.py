# coding=gbk
import pymysql
import requests,json,datetime,time
import time
import datetime
t=time.strftime("%Y-%m-%d", time.localtime())
coon = pymysql.connect(
    host = '127.0.0.1',user = 'root',passwd = 'password',
    port = 3306,db = 'databasename',charset = 'utf8'
    #port必须写int类型
    #charset必须写utf8，不能写utf-8
)
cur = coon.cursor()  #建立游标
cur.execute("sql;")  #查询数据
res = cur.fetchall()    #获取结果
count=0
for row in res:
  rf=row[1]
  rN=row[5]
  rP=row[8]
  print(rf,rN,rP)

cur.close()     #关闭游标
coon.close()    #关闭连接

def send_message(content):
    url = 'url'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "isAtAll": True
    }
    headers = {
        'Content-Type': 'application/json'
    }
    f = requests.post(url, data=json.dumps(pagrem), headers=headers,timeout=30)

def index():  
    today = datetime.date.today()
    send_message(content=str(rP))
if __name__ == '__main__':
   index()    
