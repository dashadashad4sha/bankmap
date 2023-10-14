import random

from data_atms import DATA
from street_name import extract_street_name

import sqlite3
conn = sqlite3.connect('C:/projects/more_tech_5_prototype/bankmap/db.sqlite3')
cursor = conn.cursor()

imges = ['img_atms/1.png',
         'img_atms/2.png',
         'img_atms/3.jpeg',
         'img_atms/4.jpg',
         'img_atms/5.jpeg',
         'img_atms/6.jpg']
new_data = []
for i in DATA['atms']:
    start_time = random.randint(6, 10)
    end_time = random.randint(18, 22)

    n = [
        extract_street_name(i['address']),  # title
        i['address'],  # address
        i['latitude'],  # latitude
        i['longitude'],  # longitude
        random.choice(imges),  # photo

        f"{start_time}:00",  # start_time
        f"{end_time}:00",  # end_time

        random.choice([True, False]),  # withdraw_rubles
        random.choice([True, False]),  # put_rubles
        random.choice([True, False]),  # nfc
        random.choice([True, False]),  # withdraw_qr
        random.choice([True, False]),  # qr_payment
        random.choice([True, False]),  # for_visually_impaired
        random.choice([True, False]),  # for_lm

        3,  # workload
        1,  # type
    ]
    new_data.append(n)

cursor.executemany("""INSERT INTO banks_bank (title, address, latitude, longitude, photo, start_time, end_time, withdraw_rubles, put_rubles, nfc, withdraw_qr, qr_payment, for_visually_impaired, for_lm, workload_id, type_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", new_data)
conn.commit()

conn.close()
