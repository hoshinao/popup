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


def schedule_a():
    cur.execute('SELECT * FROM schedules')
    for row in cur:
        rows = str(row[0])
        row_year = int(rows[0:4])
        row_month = int(rows[5:7])
        row_day = int(rows[8:10])
        # print(row_year,row_month,row_day)
        date_value = datetime.date(row_year, row_month, row_day)

        if date_value == datetime.date.today():
            cur.execute("SELECT schedule_action,schedule_time,place FROM schedules where schedule_year = CURRENT_DATE ")
            for rows in cur:
                print(rows)
                str_rows = ",".join(rows)
                print(rows[1])
                today_1 = datetime.datetime.today()
                today_2 = today_1.time()

                print(today_2)
                time_value = dt.strptime(rows[1], "%H:%M")
                print(type(time_value))
                print(type(today_1))
                td = (time_value - today_1)
                print(td)
                print(type(td))
                m, s = divmod(td.seconds, 60)
                h, m = divmod(m, 60)
                print(f"予定の{m}分前です")
                if m <= 30:
                    notification.notify(
                        title="スケジュール通知",
                        message=str_rows,
                        timeout=5
                    )
                else:
                    pass
    # cur.close()
    # conn.close()

schedule_a()

# 20分毎に実行
schedule.every(5).minutes.do(schedule_a)
while True:
    schedule.run_pending()
    time.sleep(1)