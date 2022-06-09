# anti-header



> info: fake chrome, firefox, opera browser header anti header

## Features

- more header params
- more request method

​	

English | [中文](./doc/README_ZH.md)

Tips:  with [anti-useragent](https://github.com/ihandmine/anti-useragent) package to use, fully compatible configuration

### Installation

```shell
pip install anti-header
```

### Usage

```python
import anti_header
from anti_header import Header
from pprint import pprint

hd = Header(platform='windows', min_version=90, max_version=100).base
hd = Header(platform='windows', min_version=90, max_version=100).random
print(anti_header.VERSION)

# must_header param useage
hd = Header(must_header={'aa': 'bb'}).random
hd = Header(must_header={'aa': 'bb'}).base

# rand_header param useage
hd = Header(rand_header={'cc': 'dd'}).random
hd = Header(rand_header={'cc': 'dd'}).base

# default_header param useage
for i in range(10):
    hd = Header(default_header={'ee': 'ff'}).base
    pprint(hd.to_unicode_dict())
    
"""
base example
{'cjito': 'azhbmf',
 'ee': 'ff',
 'referer': 'https://www.google.com/',
 'user-agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.7.3455.76 Safari/537.36'}
 
random example
{'accept-encoding': 'gzip, deflate',
 'accept-type': 'utf-8',
 'ee': 'ff',
 'origin': 'https://www.google.com/',
 'referer': 'https://www.google.com/',
 'sec-ch-ua-mobile': '?0',
 'sec-fetch-mode': 'navigate',
 'te': 'Trailers',
 'upgrade-insecure-requests': '1',
 'user-agent': 'Mozilla/5.0 (SM-G3609 Build/KTU84P; WIFI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.5.6492.87 Safari/537.36',
 'x-forwarded-for': '1',
 'xorsv': 'pvmcue'}
"""
```


If You want to  requests method useage just: 

```python
# test.py
import requests
from anti_header import Header

_url = 'https://www.google.com/'
hd = Header(url=_url, platform='windows')
requests.get(_url, header=hd.random.to_unicode_dict())

```

If You want to  scrapy downloadmiddleware method useage just: 

```python

# random_header.py
from anti_header import Header


class RandomHeaderMiddleware(object):
    def __init__(self):
        pass
    
    def process_request(request, spider):
       request.headers = Headers(url=request.url).random
    
    def process_response(request, response, spider):
        return response
```

If You want to  specify param just: 

```python
from anti_header import Header
hd = Header(logger=True)

# the default install loguru
try:
    from loguru import logger
except:
    install("loguru")
    from loguru import logger
    
# close default singleton
hd = Header(dry=True)

```



Make sure that You using latest version

```
pip install -U anti-header
```

Check version via python console: 

```
import anti_header

print(anti_header.VERSION)
```

