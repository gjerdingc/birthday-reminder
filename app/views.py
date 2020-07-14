from tinydb import TinyDB, Query
from datetime import datetime, date
# from dateutil import parser, relativedelta
# from operator import itemgetter

from flask import Flask
from flask import render_template

app = Flask(__name__)

db = TinyDB('birthdays.db')

class Person:
    def __init__(self, givenName, surname, birthdate):

       self.givenName = givenName
       self.surname = surname
       self.birthdate = birthdate


@app.route('/')
def home():
   personList = []

   for i in db.all():
      bdayObject = datetime.strptime(i['birthdate'], '%d%m%y')
      bdayformatted = bdayObject.strftime("%d %b %Y")

      person = Person(i['givenName'], i['surName'], bdayformatted)

      personList.append(person)


   return render_template('index.html', personList = personList)




# for person in people:
#     bdayObject = datetime.strptime(person['birthdate'], '%d%m%y')
#     bdayObject = datetime(datetime.now().year, bdayObject.month, bdayObject.day)
#     person['birthdate'] = bdayObject

#     print(person)


# people.sort(key = lambda x: x['birthdate'])

# print('\n\n')
# td = people[6]['birthdate'] - datetime.now()
# print(td.days)

# print('\n\n')
# for person in people:
#     print(person)





if __name__ == "__main__":
    app.run(host='0.0.0.0')