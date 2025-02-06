import sqlite3

db_path = 'F:\\Cache\\python\\ent.db'

def create_table():
    conn = sqlite3.connect(db_path)

    curs = conn.cursor()

    curs.execute('''
            CREATE TABLE zoo(
                id VARCHAR(20) PRIMARY KEY,
                count INT,
                damage FLOAT
            )
        ''')

    curs.close()

def insert():
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    insert_sql_template = 'insert into zoo (id, count, damage) values(?,?,?)'
    curs.execute('insert into zoo (id, count, damage) values("1",2,3)')
    curs.execute(insert_sql_template, ('122', 1, 200.9))

    conn.commit()

    curs.close()

def query():
    conn = sqlite3.connect(db_path)

    curs = conn.cursor()
    curs.execute('SELECT * from zoo order by count asc')
    rows = curs.fetchall()
    print(rows)

    curs.close()

if __name__ == "__main__":
    # create_table()

    # insert()

    query()