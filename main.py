from plyer import notification
import schedule
import time
import sqlite3
import datetime

def job(cur):
    alert = ""

    cur.execute("select schedule_action from schedules order by schedule_date limit 1")
    rows = cur.fechall()
    print(rows)
    hoge = rows[0][0]
    print(hoge)

    dt = datetime.date.today()
    #yyyy-mm-dd
    #yyyy-mm-dd hh:mm:ss

    if int(hoge) == dt:

con = sqlite3.connect("./schedule.db")
cur = con.cursor()
schedule.every(10).second.do(job,cur)



# notification.notify(
#     title="Pythonで通知",
#     message="テスト通知",
#     app_name="アプリの名前",
#     timeout=5
# )