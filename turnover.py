 #--coding:GBK --
import cx_Oracle


import requests,json,datetime,time

#conn = cx_Oracle.connect('EDAVIEWER/EDAVIEWER123@MESEA')

conn = cx_Oracle.connect(user='system',password='manager',dsn='st1719')

cursor = conn.cursor()


ret = cursor.execute("""select sum(t.amount) as amount from stdba.divi_time_stat t where t.work_date=trunc(sysdate) order by t.interval""")

#content=cursor.getColumnIndex("amount")
content=cursor.fetchone()
cursor.close()
conn.close()

def send_message(content):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=e4a66d0a0a158cd4441b9b84f35fd9d5981d0f209175d437776f123325a058ed'
    pagrem = {
        "msgtype": "text",
        "text": {
        "content": content
    },
    "at": {
         "isAtAll": False     #@全体成员（在此可设置@特定某人）
    }
    }
    headers = {
        'Content-Type': 'application/json',
    }
    f = requests.post(url, data=json.dumps(pagrem), headers=headers)

def index():  
    today = datetime.date.today()
    send_message(content=str(today)+"东海店当前业绩为: "+format(content))
if __name__ == '__main__':
   index() 
  #while True:
        #try:
            
            #time.sleep(60)
        #except Exception as e:
           # print(e)
           # continue
