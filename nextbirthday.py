from tinydb import TinyDB, Query
from datetime import datetime, date
from dateutil import parser, relativedelta
from operator import itemgetter

db = TinyDB('/home/pi/bin/database/birthdays.db')

people = db.all()

for person in people:
    bdayObject = datetime.strptime(person['birthdate'], '%d%m%y')
    bdayObject = datetime(datetime.now().year, bdayObject.month, bdayObject.day)
    person['birthdate'] = bdayObject

    print(person)


people.sort(key = lambda x: x['birthdate'])

print('\n\n')
td = people[6]['birthdate'] - datetime.now()
print(td.days)

print('\n\n')
for person in people:
    print(person)