from tinydb import Query,TinyDB,where
import re
db = TinyDB('main.json')
data = Query()
def insert(user,age,location):
    for i in db.all():
        if (i['Name'] == user.title()) and (i['Age'] == age) and (i['Location'] == location.title()):
            print(('Already exists the database entry'))
            return
    else:
        db.insert({'Name':user.title(),'Age':age,'Location':location.title()})#
        print('database updated')

def delete(user,age,location):
    db.remove((data.Name == user) and (data.Age == age) and (data.Location == location))

def update(target,user=None,age=None,location=None):
    if user != None:
        db.update({'Name':target.title()},data.Name==user.title())
    elif age != None:
        db.update({'Name':target.title()},data.Name==age)
    elif location != None:
        db.update({'Name':target.title()},data.Name==location.title())
    else:
        print('Be clear')

def search(user=None,age=None,location=None):
    if user != None:
        print(db.search(data.Name == user.title()))
    if age != None:
        print(db.search(data.Age == age))
    if location != None:
        print(db.search(data.Location == location.title()))


print(db.search(data.Age > 21))

#remove the all database
#db.truncate()

#create Table
#table =db.table('table Name')

#del table
#db.drop_table(Table Name)

