import mysql.connector
config = {
    'user': 'root',
    'password': 'Lokgpt031',
    'host': 'localhost',
    'database':'acme'
}
db = mysql.connector.connect(**config)
cursor=db.cursor()