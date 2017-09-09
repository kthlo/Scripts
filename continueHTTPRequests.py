#randomHTTPRequests.py
#Continue sending HTTP requests to keep connection alive

import requests
import time
import sys

#url to send requests to
url = 'http://google.com'
#time(seconds) between requests
pauseTime = 15
timeElapsed = 0 

try:
    while True:
        r = requests.get(url)
        print('Running, Connection Status:', r.status_code, ', Ctrl+C to terminate')
        print('Time Elapsed: ', int(timeElapsed/60), 'minutes', int(timeElapsed%60), 'seconds')
        time.sleep(pauseTime)
        timeElapsed += pauseTime
except KeyboardInterrupt: #terminate script
    print('Terminated')
except Exception as e:
  print('Error:', sys.exc_info()[0])
