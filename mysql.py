# coding=gbk
import pymysql
import requests,json,datetime,time
import time
import datetime
t=time.strftime("%Y-%m-%d", time.localtime())
coon = pymysql.connect(
    host = '127.0.0.1',user = 'root',passwd = 'auchan',
    port = 3306,db = 'rt-mart',charset = 'utf8'
    #port����дint����
    #charset����дutf8������дutf-8
)
cur = coon.cursor()  #�����α�
cur.execute("select * from rf_information as t1,(select max(rtime),rcode,rpath from rf_records group by rcode)as t where t1.rcode=t.rcode and t1.rstate='����'and datediff(current_date(),rtime)>=2;")  #��ѯ����
res = cur.fetchall()    #��ȡ���
count=0
for row in res:
  rf=row[1]
  rN=row[5]
  rP=row[8]
  print(rf,rN,rP)

cur.close()     #�ر��α�
coon.close()    #�ر�����

def send_message(content):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bcd8b541debeb4aa70f1a1a093abfb20565336b841fa18f9455ed060e682cb18'
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
