import mysql.connector
from mysql.connector import errorcode
from config import cursor

DB_NAME ='ACME'
TABLES={}

TABLES['logs']=(
    'CREATE TABLE `logs`('
    "`ID` INT(11) NOT NULL AUTO_INCREMENT,"
    "`TEXT` VARCHAR(255) NOT NULL,"
    "`USER` VARCHAR(255) NOT NULL,"
    "`CREATED` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY(`ID`)"
    ") ENGINE=InnoDB"
)
def create_database(dbname):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname} DEFAULT CHARACTER SET 'utF8'")
    print(f"database created successfully {dbname}")


def create_table(dbname):
    cursor.execute(f'USE {dbname}')
    for table_name in TABLES:
        table_description=TABLES[table_name]
        try:
            cursor.execute(table_description)
            print(f"Creating table {table_name}",end='')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists")
            else:
                print(err.msg)



create_database(DB_NAME)
create_table(DB_NAME)