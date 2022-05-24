import sqlite3

connection = sqlite3.connect('hostel.db')

cursor = connection.cursor()


# Создание таблиц.
def create_tables():
    # Создаем таблицу комнат.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Room
                  (number INTEGER NOT NULL PRIMARY KEY, 
                  class TEXT NOT NULL,
                  cost INTEGER DEFAULT NULL,
                  number_of_bed INT NOT NULL,
                  FOREIGN KEY (class) REFERENCES Class_Room (class)
                  )''')

    # Создаем таблицу постояльцев.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Resident
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  name TEXT NOT NULL,
                  id_organization INTEGER DEFAULT NULL,
                  phone_number INTEGER DEFAULT NULL,
                  passport_details INTEGER NOT NULL,
                  FOREIGN KEY (id_organization) REFERENCES Organization (id)
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
                  room INTEGER NOT NULL, 
                  time_change TEXT NOT NULL,
                  date_change TEXT NOT NULL,
                  id_working_employee INTEGER NOT NULL,
                  FOREIGN KEY (id_working_employee) REFERENCES Working_Employee (id)
                  )''')

    # Создаем таблицу броней.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Reservation
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  id_resident INTEGER NOT NULL, 
                  check_out_date TEXT NOT NULL,
                  check_in_date TEXT NOT NULL,
                  room INTEGER NOT NULL,
                  prepay INTEGER NOT NULL,
                  FOREIGN KEY (id_resident) REFERENCES Resident (id),
                  FOREIGN KEY (room) REFERENCES Room (number)
                  )''')

    # Создаем таблицу сотрудников.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  name TEXT NOT NULL, 
                  position TEXT NOT NULL,
                  phone_number INTEGER DEFAULT NULL,
                  passport_details INTEGER NOT NULL,
                  FOREIGN KEY (position) REFERENCES Employee (id)
                  )''')

    # Создаем таблицу работающих сотрудников.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Working_Employee
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  id_employee INTEGER NOT NULL, 
                  shift_start_date TEXT NOT NULL,
                  shift_start_time TEXT NOT NULL,
                  shift_time TEXT DEFAULT NULL,
                  FOREIGN KEY (id_employee) REFERENCES Employee (id)
                  )''')

    # Создаем таблицу Должностей
    cursor.execute('''CREATE TABLE IF NOT EXISTS Position
                  (position TEXT NOT NULL PRIMARY KEY, 
                  wage_rate INT NOT NULL
                  )''')

    # Создаем таблицу Классов номеров.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Class_Room
                      (class TEXT NOT NULL PRIMARY KEY, 
                      base_cost INT NOT NULL,
                      added_value INT NOT NULL
                      )''')

    # Создаем таблицу Кодов состояний.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Code_Status
                         (status_code INTEGER NOT NULL PRIMARY KEY, 
                         name_status TEXT NOT NULL
                         )''')


# Заполнение таблиц.
def fill_tables():
    # Заполнение данными таблицу комнат
    rooms = open('data/room.txt')
    for line in rooms:
        separate_line = line.split('/')
        for i in range(int(separate_line[0])):
            data = separate_line[1] + ',' + separate_line[2]
            cursor.execute(f'''INSERT INTO Room
                (class, number_of_bed)
                VALUES({data})
                ''')

    # Заполнение данными таблицу классов номеров
    class_room = open('data/class_room.txt')
    for line in class_room:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1] + ',' + separate_line[2]
        cursor.execute(f'''INSERT INTO Class_Room
            (class, base_cost, added_value)
            VALUES({data})
            ''')

    # Заполнение данными таблицу работников
    employee = open('data/employee.txt')
    for line in employee:
        print(line)
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1] + ',' + separate_line[2] + ',' + separate_line[3]
        cursor.execute(f'''INSERT INTO Employee
            (name, position, phone_number, passport_details)
            VALUES({data})
            ''')

    # Заполнение данными таблицу должностей
    position = open('data/position.txt')
    for line in position:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1]
        cursor.execute(f'''INSERT INTO Position
            (position, wage_rate)
            VALUES({data})
            ''')

    # Заполнение данными таблицу работников на смене
    working_employee = open('data/working_employee.txt')
    for line in working_employee:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1] + ',' + separate_line[2] + ',' + separate_line[3]
        cursor.execute(f'''INSERT INTO Working_Employee
            (id_employee, shift_start_date, shift_start_time, shift_time)
            VALUES({data})
            ''')

    # Заполнение данными таблицу постояльцев
    resident = open('data/resident.txt')
    for line in resident:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1] + ',' + separate_line[2] + ',' + separate_line[3]
        cursor.execute(f'''INSERT INTO Resident
            (name, id_organization, phone_number, passport_details)
            VALUES({data})
            ''')

    # Заполнение данными таблицу организаций
    organization = open('data/organization.txt')
    for line in organization:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1]
        cursor.execute(f'''INSERT INTO Organization
            (name, type)
            VALUES({data})
            ''')

    # Заполнение данными таблицу кодов состояний
    status_code = open('data/status_code.txt')
    for line in status_code:
        print(line)
        cursor.execute(f'''INSERT INTO Code_Status
            (name_status)
            VALUES({line})
            ''')

    # Заполнение данными таблицу состояний
    status = open('data/status.txt')
    for line in status:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1] + ',' + separate_line[2] + ',' + separate_line[3] + \
            ',' + separate_line[4]
        cursor.execute(f'''INSERT INTO Status
            (status_code, room, time_change, date_change, id_working_employee)
            VALUES({data})
            ''')

    # Заполнение данными таблицу броней
    reservation = open('data/reservation.txt')
    for line in reservation:
        separate_line = line.split('/')
        data = separate_line[0] + ',' + separate_line[1] + ',' + separate_line[2] + ',' + separate_line[3] +\
            ',' + separate_line[4]
        cursor.execute(f'''INSERT INTO Reservation
            (id_resident, check_in_date, check_out_date, room, prepay)
            VALUES({data})
            ''')


create_tables()
fill_tables()

connection.commit()
connection.close()
