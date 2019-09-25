import requests,json,datetime,time
import xlrd
def send_message(content):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=e4a66d0a0a158cd4441b9b84f35fd9d5981d0f209175d437776f123325a058ed'
    pagrem = {
        "msgtype": "text",
        "text": {
        "content": content
    },
    "at": {
         "isAtAll": True     #@全体成员（在此可设置@特定某人）
    }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    f = requests.post(url, data=json.dumps(pagrem), headers=headers)



def index():
    today = datetime.date.today()
    #获取当天是周几
    todayweek = datetime.date.isoweekday(today)
    
    #读取EXCEL
    IO =  'D:\python\project\duty.xlsx'
    wb = xlrd.open_workbook(filename=IO)
    #读取第一张表名
    sheet1 = wb.sheet_by_index(0)
    print(wb.sheet_names())
    
    
    #print("获取到所有的值:\n{0}".format(data))
    
    #利用IF语句判断周几选出当天要发送的文案
    Copywriting = "今日IT值班人员:"
    if todayweek == 1:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,1).value)+" \n 晚班值班:"+ str(sheet1.cell(2,1).value)+"\n")
    elif todayweek == 2:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,2).value)+" \n 晚班值班:"+ str(sheet1.cell(2,2).value)+"\n")
    elif todayweek == 3:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,3).value)+" \n 晚班值班:"+ str(sheet1.cell(2,3).value)+"\n")
    elif todayweek == 4:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,4).value)+" \n 晚班值班:"+ str(sheet1.cell(2,4).value)+"\n")
    elif todayweek == 5:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,5).value)+" \n 晚班值班:"+ str(sheet1.cell(2,5).value)+"\n")
    elif todayweek == 6:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,6).value)+" \n 晚班值班:"+ str(sheet1.cell(2,6).value)+"\n")
    elif todayweek == 7:
        send_message(content=""+ Copywriting + "\n 早班值班:"+format(sheet1.cell(1,7).value)+" \n 晚班值班:"+ str(sheet1.cell(2,7).value)+"\n")
     

if __name__ == '__main__':
   index() 
  #while True:
        #try:
            
            #time.sleep(60)
        #except Exception as e:
           # print(e)
           # continue
