# Grafana admin BulatRuleZ777
import requests
# import sqlite3
import psycopg2
import pytz
from datetime import datetime


# conn = sqlite3.connect('zireael.db')

conn = psycopg2.connect(dbname='zireael_db', user='zireael', password='zireael', host='localhost')

cursor = conn.cursor()
sql = 'SELECT * FROM public."zireaelApp_node" limit 100'
cursor.execute(sql)
print(cursor.fetchone())


headers = {
    'Accept': 'application/json',
    'Authorization': 'key ttn-account-v2.1g4tMxV7hWUI64gnAPC70b38LNzH-XxV0Aduz81e_dY',
}
resp = requests.get(
    "https://zireael.data.thethingsnetwork.org/api/v2/query?last=30m", headers=headers)
if resp.status_code != 200:
    print("Error: " + str(resp))


for note in resp.json():
    t = (note['device_id'],)
    cursor.execute("""
        select 
            id
        from 
            public."zireaelApp_node"
        where 
            "ttnDevId"=%s
        """, t)
    node_id = cursor.fetchone()[0]

    t = (note['time'],)
    cursor.execute("""
        SELECT COUNT 
            (*)
        FROM 
            public."zireaelApp_log" 
        WHERE 
            "ttnTime"=%s
        """, t)
    num = cursor.fetchone()[0]
    print(num)
    if num == 0:
        t = (
            note['time'],
            datetime.now(),
            str(node_id),
            note['h0'],
            note['h1'],
            note['h2'],
            note['h3'],
            note['t0'],
            note['t1'],
            note['t2'],
            note['t3'],
            note['vbat'],
        )
        cursor.execute("""
            INSERT INTO 
                public."zireaelApp_log"(
                    "ttnTime", 
                    "localTime",
                    node_id,
                    humidity_0,
                    humidity_1,
                    humidity_2,
                    humidity_3,
                    temperature_0,
                    temperature_1,
                    temperature_2,
                    temperature_3,
                    battery)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", t)
        
        print("Successfully added data")


conn.commit()
