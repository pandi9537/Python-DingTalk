 #--coding:GBK --
import cx_Oracle


import requests,json,datetime,time

#conn = cx_Oracle.connect('EDAVIEWER/EDAVIEWER123@MESEA')

conn = cx_Oracle.connect(user='system',password='manager',dsn='st1719')

cursor = conn.cursor()


ret = cursor.execute("""sql""")

#content=cursor.getColumnIndex("amount")
content=cursor.fetchone()
cursor.close()
conn.close()

def send_message(content):
    url = ''
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
    send_message(content=str(today)+"test"+format(content))
if __name__ == '__main__':
   index() 
  #while True:
        #try:
            
            #time.sleep(60)
        #except Exception as e:
           # print(e)
           # continue
