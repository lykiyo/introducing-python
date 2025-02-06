import pymysql as mysql

def create_table():
    conn = mysql.connect(host="127.0.0.1",port=13306,user="root",password="123456", database="learnlab")

    curs = conn.cursor()

    curs.execute('''
        CREATE TABLE zoo(
            id VARCHAR(40) PRIMARY KEY,
            count INT,
            damage FLOAT
        )
    ''')

    conn.commit()

    curs.close()

def insert_data():
    conn = mysql.connect(host="127.0.0.1", port=13306, user="root", password="123456", database="learnlab")
    try:
        curs = conn.cursor()
        insert_sql_template = 'insert into zoo (id, count, damage) values (%s,%s,%s)'
        # curs.execute('insert into zoo (id, count, damage) values("1",2,3)')
        curs.execute(insert_sql_template, ('122', 1, 200.9))

        conn.commit()
        curs.close()
    except Exception as e:
        print(e)
        conn.rollback()

def query_data():
    conn = mysql.connect(host="127.0.0.1", port=13306, user="root", password="123456", database="learnlab")
    curs = conn.cursor()
    curs.execute("SELECT * from zoo")

    rows = curs.fetchall()

    print(rows)

    curs.close()



if __name__ == "__main__":
    # create_table()

    # insert_data()

    query_data()