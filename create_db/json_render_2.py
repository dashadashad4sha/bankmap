import random

from offices import DATA

import sqlite3

conn = sqlite3.connect('C:/projects/more_tech_5_prototype/bankmap/db.sqlite3')
cursor = conn.cursor()

imges = ['img_off/1.jpg',
         'img_off/2.jpg',
         'img_off/3.jpg',
         'img_off/4.jpg',
         'img_off/5.jpg',
         'img_off/6.jpg']
new_data = []
for i in DATA[5:]:
    start_time = random.randint(6, 10)
    end_time = random.randint(18, 22)

    n = [
        i['salePointName'],  # title
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
        2,  # type
    ]
    new_data.append(n)

cursor.executemany("""INSERT INTO banks_bank (title, address, latitude, longitude, photo, start_time, end_time, withdraw_rubles, put_rubles, nfc, withdraw_qr, qr_payment, for_visually_impaired, for_lm, workload_id, type_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", new_data)
conn.commit()

conn.close()