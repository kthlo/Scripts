#randomHTTPRequests.py
#Continue sending HTTP requests to keep connection alive

import requests
import time

#url to send requests to
url = 'http://google.com'
#time(seconds) between requests
pauseTime = 15
timeElapsed = 0 

try:
    while True:
        requests.get(url)
        print('Script Running, Ctrl+C to terminate')
        print('Time Elapsed: ', int(timeElapsed/60), 'minutes', int(timeElapsed%60), 'seconds')
        time.sleep(pauseTime)
        timeElapsed += pauseTime
except KeyboardInterrupt:
    print('Terminated')
