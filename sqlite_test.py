import sqlite3
import uuid

db_name = "students.db"
conn = sqlite3.connect(db_name)
cur = conn.cursor()
print(f"connected to {db_name}")


def create_teacher_table():
    sql_cmd = """create table teacher(
    uid varchar(40) primary key,
    name varchar(30) not null,
    address varchar(100)
    )"""
    cur.execute(sql_cmd)
    # cur.fetchone()


def add_record_teacher(name, address):
    uid = str(uuid.uuid4())
    print(f"adding record: ({uid}, {name}, {address})")
    sql_cmd = f"insert into 'teacher' ('uid', 'name', 'address') values ('{uid}', '{name}', '{address}')"
    cur.execute(sql_cmd)


def print_all_records():
    sql_cmd = "select uid, name, address from teacher;"
    cur.execute(sql_cmd)
    teachers = cur.fetchall()
    # print(f"teacher: {teachers}")
    print(f"count of teacher: {len(teachers)}")


# print("creating the teacher table")
# create_teacher_table()

print("adding records:")
add_record_teacher("Ramesh", "1 First Street")
add_record_teacher("Suresh", "2 Second Road")
add_record_teacher("Kumar", "3 Third avenue")

print("print all records of teacher table:")
print_all_records()

conn.commit()
conn.close()
