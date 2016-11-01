from django.db import connection

print 'Creating and initializing database...'

with connection.cursor() as cursor:
    cursor.execute('CREATE TABLE rooms (ID INTEGER PRIMARY KEY AUTOINCREMENT, ROOMNUMBER TEXT)')
    cursor.execute("INSERT INTO rooms (ROOMNUMBER) VALUES ('H-905')")
    cursor.execute("INSERT INTO rooms (ROOMNUMBER) VALUES ('H-831')")
    cursor.execute("INSERT INTO rooms (ROOMNUMBER) VALUES ('H-747')")
    cursor.execute('CREATE TABLE users (ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME TEXT, PASSWORD TEXT)')
    cursor.execute("INSERT INTO users (USERNAME,PASSWORD) VALUES ('testuser','test')")
    cursor.execute("INSERT INTO users (USERNAME,PASSWORD) VALUES ('John','password123')")
    cursor.execute('CREATE TABLE reservations (USER_ID INT REFERENCES users(ID), ROOM_ID INT REFERENCES rooms(ID),\
            STATUS TEXT, TIMESLOT TEXT, TIMESTAMP TEXT)')
    cursor.execute("INSERT INTO reservations (USER_ID,ROOM_ID,STATUS,TIMESLOT,TIMESTAMP) \
            VALUES (1,1,'filled','2016-10-28T130000Z', '2016-10-27T145420Z')")


print 'Database setup has been completed.'
