from crawler import main
import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token        
    }

    payload = {
        "message": msg
    }

    r = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)

    print(r.status_code)


if __name__ == "__main__":
    
    token = 'pj4zAv0SHrx80RGRQ3gINSg6nfOBbzgLdgsReqQGxNN'
    msg = 'Testing!'
    lineNotifyMessage(token, msg)