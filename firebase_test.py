import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import time


cred = credentials.Certificate('serviceAccount.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facebook-crawler-2b822-default-rtdb.firebaseio.com/'
})

payload = {
        'name': 'kid4',
        'email': 'qq4@gmail.com'
}


dateTime = datetime.now()
datestamp = dateTime.strftime("%d-%b-%Y")
# print(datestamp)
k = '' + '螢幕'
ref = db.reference('/'+datestamp+'/'+k+'/')
data = ref.get()
# print(len(data))
print(data[0]['content'])

dictlist = []
for key, value in data.items():
    temp = [key,value]
    dictlist.append(temp)

print(dictlist[0][1]['content'])
