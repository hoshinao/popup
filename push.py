import schedule
import datetime
import sqlite3
import time
from datetime import datetime as dt
from plyer import notification


dbname = "schedule.db"
conn = sqlite3.connect(dbname)

cur = conn.cursor()

def push_on():
    cur.execute('SELECT * FROM schedules')
    for row in cur:
        rows = str(row[0])
        row_year = int(rows[0:4])
        row_month = int(rows[5:7])
        row_day = int(rows[8:10])
        # print(row_year,row_month,row_day)
        date_value = datetime.date(row_year, row_month, row_day)

        if date_value == datetime.date.today():
            cur.execute("SELECT schedule_action,schedule_time,place,push FROM schedules where schedule_year = CURRENT_DATE ")

            for rows in cur:
                str_rows = ",".join(rows)
                print(str_rows)
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

                for rex in rows[0:3]:
                    rexs = " ".join(rex)
                    print(f"確認{rexs}")

                # cur.execute("SELECT push FROM schedules where schedule_year = CURRENT_DATE ")
                # for flug in cur:
                #     print(flug[0])

                if m <= 30 and rows[3] == "未":
                    notification.notify(
                        title="スケジュール通知",
                        message=str_datas,
                        timeout=5
                    )

                    # sql = """UPDATE schedules SET push="済" WHERE ? = "未"　and ? <= 30 """
                    # pal = rows[3]
                    # min = m
                    # cur.execute(sql,pal,min)
                    # conn.commit()
                else:
                    pass

    # cur.close()
    # conn.close()
push_on()

# 5分毎に実行
schedule.every(5).minutes.do(push_on)
while True:
    schedule.run_pending()
    time.sleep(1)
