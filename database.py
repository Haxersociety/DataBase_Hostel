import sqlite3

connection = sqlite3.connect('hostel.db')

cursor = connection.cursor()


# Создание таблиц.
def create_tables():
    # Создаем таблицу комнат.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Room
                  (number INTEGER NOT NULL PRIMARY KEY, 
                  id_status INTEGER NOT NULL, 
                  class TEXT NOT NULL,
                  cost INTEGER NOT NULL,
                  number_of_bed TEXT NOT NULL
                  )''')

    # Создаем таблицу постояльцев.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Resident
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  id_last_reservation INTEGER NOT NULL, 
                  name TEXT NOT NULL,
                  id_organization INTEGER NOT NULL,
                  phone_number INTEGER NOT NULL,
                  passport_details TEXT NOT NULL
                  )''')

    # Создаем таблицу организаций.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Organization
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  name TEXT NOT NULL, 
                  type TEXT NOT NULL
                  )''')

    # Создаем таблицу состояний.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Status
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  status_code INTEGER NOT NULL, 
                  time_change TEXT NOT NULL,
                  date_change TEXT NOT NULL,
                  id_working_employee INTEGER NOT NULL,
                  FOREIGN KEY(id_working_employee) REFERENCES Working_Employee(id)
                  )''')

    # Создаем таблицу броней.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Reservation
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  id_resident INTEGER NOT NULL, 
                  check_out_date TEXT NOT NULL,
                  check_in date TEXT NOT NULL,
                  room_number INTEGER NOT NULL,
                  prepay INTEGER NOT NULL
                  )''')

    # Создаем таблицу сотрудников.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  name TEXT NOT NULL, 
                  position TEXT NOT NULL,
                  salary INTEGER NOT NULL,
                  passport_details TEXT NOT NULL
                  )''')

    # Создаем таблицу работающих сотрудников.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Working_Employee
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  id_employee INTEGER NOT NULL, 
                  shift_start_date TEXT NOT NULL,
                  shift_start_time TEXT NOT NULL,
                  shift_time TEXT NOT NULL
                  )''')


create_tables()

# Заполнение данными таблицу комнат
rooms = open('data/room.txt')
for line in rooms:
    separate_line = line.split('/')
    for i in range(int(separate_line[0])):
        data = separate_line[1]+','+separate_line[2]+','+separate_line[3]+','+separate_line[4]
        cursor.execute(f'''INSERT INTO Room
            (id_status, class, cost, number_of_bed)
            VALUES({data})
            ''')

# Заполнение данными таблицу комнат
rooms = open('data/room.txt')
for line in rooms:
    separate_line = line.split('/')
    for i in range(int(separate_line[0])):
        data = separate_line[1]+','+separate_line[2]+','+separate_line[3]+','+separate_line[4]
        cursor.execute(f'''INSERT INTO Room
            (id_status, class, cost, number_of_bed)
            VALUES({data})
            ''')


connection.commit()
connection.close()
