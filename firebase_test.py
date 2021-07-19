import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('serviceAccount.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facebook-crawler-2b822-default-rtdb.firebaseio.com/'
})

payload = {
        'name': 'kid4',
        'email': 'qq4@gmail.com'
}

ref = db.reference('/User_02/')
ref.delete()