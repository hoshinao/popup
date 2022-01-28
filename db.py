import sqlite3
import datetime
import time
from plyer import notification
import schedule
import time
import sqlite3
import datetime
from datetime import datetime as dt

dbname = "schedule.db"
conn = sqlite3.connect(dbname)

cur = conn.cursor()

# テーブル作成
# cur.execute("CREATE TABLE schedules(schedule_date date,schedule_time time,schedule_action STRING)")

def schedule_check(tval_1, tval_2, tval_3, tval_4):
    n1 = tval_1
    n2 = tval_2
    n3 = tval_3
    n4 = tval_4
    # データ作成
    sql = """INSERT INTO schedules(schedule_year,schedule_action,schedule_time,place)VALUES(?,?,?,?)"""
    data_set = n1, n2, n3, n4
    cur.execute(sql, data_set)
    conn.commit()