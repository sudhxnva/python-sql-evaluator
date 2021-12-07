import os
import sqlite3

dirname = os.path.dirname(os.path.abspath(__file__))

db = sqlite3.connect(os.path.abspath(os.path.join(
    dirname, 'db', 'employee.db')))

def create():
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE Manager(
                mgr_id varchar(25) NOT NULL,
                PRIMARY KEY(mgr_id)
                )""")

    cursor.execute("""CREATE TABLE Employees(
                emp_id varchar(25) NOT NULL,
                emp_name varchar(25) NOT NULL,
                role varchar(25) NOT NULL,
                mgr_id varchar(25),
                PRIMARY KEY(emp_id),
                FOREIGN KEY(mgr_id) REFERENCES Manager(mgr_id)
                )""")

    db.commit()


def insert():
    cursor = db.cursor()
    cursor.execute("""INSERT INTO Manager VALUES('#mgr1')""")
    cursor.execute("""INSERT INTO Manager VALUES('#mgr2')""")
    cursor.execute("""INSERT INTO Manager VALUES('#mgr3')""")

    cursor.execute("""INSERT INTO Employees VALUES('#emp1','Bruce Wayne','Manager','#mgr1')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp2','Robert Brick','Employee','#mgr1')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp3','TinTin','Employee','#mgr1')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp4','Denim Gauge','Employee','#mgr1')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp5','Clark Kent','Manager','#mgr2')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp6','Daniel Dim','Employee','#mgr2')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp7','Ben Drool','Manager','#mgr3')""")
    cursor.execute("""INSERT INTO Employees VALUES('#emp8','Tracy McGreen','Employee','#mgr3')""")

    db.commit()


create()
insert()
db.close()
