#get all images from the craigslist post with URL
from urllib.request import urlretrieve
import requests
import json
from bs4 import BeautifulSoup
import sys
if (len(sys.argv) == 2):
  url = sys.argv[1]
else:
  raise ValueError('Format: python get_img.py [url]')

r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
script_tags = soup.find_all('script')
imgid_text = ''
for script in script_tags:
  if 'imgList' in str(script.string):
    imgid_text = str(script.string)[18:-5]
    break
imgList_json = json.loads(imgid_text)
count = 1
for item in imgList_json:
  id = item['imgid'][2:]
  urlretrieve('https://images.craigslist.org/'+id+'_1200x900.jpg', str('%02d' % count)+'.jpg')
  print('img #' + str(count) + ' downloaded')
  count += 1
print('Images Total: ' + str(count - 1))
