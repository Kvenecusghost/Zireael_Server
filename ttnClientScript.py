# Grafana admin BulatRuleZ777
import requests
import sqlite3
import psycopg2


conn = sqlite3.connect('zireael.db')

# conn = psycopg2.connect()

cursor = conn.cursor()
sql = "SELECT * FROM devices limit 100"
ret = cursor.execute(sql)
print(ret.fetchall())


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
    device_id = cursor.execute(
        'SELECT id FROM devices WHERE dev_id=?', (note['device_id'],)).fetchone()[0]

    t = (note['time'],)
    num = cursor.execute("""SELECT COUNT (*)
            FROM data WHERE time=?""", t).fetchone()[0]
    if num == 0:
        t = (
            note['time'],
            str(device_id),
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
        cursor.execute("""INSERT INTO data(time, 
                                            device_id,
                                            humidity_0,
                                            humidity_1,
                                            humidity_2,
                                            humidity_3,
                                            temperature_0,
                                            temperature_1,
                                            temperature_2,
                                            temperature_3,
                                            battery)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?)""", t)
        print("Successfully added data")
    # print(devId)


#     sql =   """INSERT INTO data(time, device_id)
#                 VALUES(0, 0, 0)
#             """
#     sqlnote =

#     print(note)


conn.commit()
