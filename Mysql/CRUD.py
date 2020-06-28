from config import cursor,db

def add_log(text, user):
    sql=("INSERT INTO logs(TEXT,USER) VALUES (%s,%s)")
    cursor.execute(sql,(text,user))
    db.commit()
    log_id=cursor.lastrowid
    print(f'Added log entry-->{log_id}')

def get_logs():
    sql = ("SELECT * FROM logs  order by created ")
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
def get_log(id):
    sql = ("SELECT * FROM logs where id = %s order by created ")
    try:
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        for row in result:
            print(row)
    except TypeError:
        print('Entered id is not present in table')

def delete(id):
    sql = "delete from logs where id = %s"
    cursor.execute(sql,(id,))
    db.commit()
    print('logs deleted from database successfully.')


def update(text,id):
    sql = (f"update logs set text = %s where id = %s")
    cursor.execute(sql,(text,id))
    db.commit()
    print(f'update log entry-->where id = {id}')

# add_log('This is the first log entry.','Lokesh')
# add_log('This is the second log entry.','Bhanu')
# add_log('This is the third log entry.','Hari_Priya')
#
# get_logs()
# update('This is the fifth log entry.',5)
# get_log(7)
# delete(7)
