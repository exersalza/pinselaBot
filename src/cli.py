from datetime import datetime
from time import sleep
from pytz import timezone
import threading

tz = timezone('Europe/Berlin')


def action1():
    while True:
        print(f'Clock: {datetime.now(tz=tz).strftime("%H:%M:%S")}', end='\r')
        sleep(1)


starter = threading.Thread(target=action1)
starter.start()
