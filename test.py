from datetime import datetime
import time



while True:
    dateTime = datetime.now()
    timestampStr = dateTime.strftime("%d-%b-%Y | %H:%M:%S.%f")
    print(timestampStr)
    time.sleep(1)