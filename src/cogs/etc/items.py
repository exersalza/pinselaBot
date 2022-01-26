# here comes the item functions :)
import sys
import time
from datetime import datetime

import pytz
from pytz import timezone

try:
    while True:
        print(f'Current time: {datetime.now(timezone(sys.argv[1])).strftime("%H:%M:%S - %d.%m.%Y")}', end='\r')
        time.sleep(1)

except pytz.UnknownTimeZoneError:
    print('Timezone is Unknown')


