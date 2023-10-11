#!/usr/bin/env python
# coding: utf-8

# In[33]:


import requests

url = 'http://localhost:8000/'

headers = {
    'Host': 'localhost:8000',
    'Cookie': '_gat=2; PHPSESSID=6dcdac1b10a3f431a6aa93ec036c0e2b7df2efea2a00d901c500b05400acdd56; _ga=GA1.2.1226339203.1695178640; _gid=GA1.2.1794003679.1695178640',
     'User-Agent': 'ABCD-1234'
}

response = requests.get(url, headers=headers)

print(response.text)
import requests

url = 'http://localhost:8000/'

headers = {
    'Host': 'localhost:8000',
    'Cookie': '_gat=27; PHPSESSID=837afd29ec53250709121fa1fe0ff515016980b908ce0de23cc3d49b0cec2d3d; _ga=GA1.2.1226339203.1695178640; _gid=GA1.2.1794003679.1695178640',
    'User-Agent': 'ABCD-1234 72.101.108.108'
}

response = requests.get(url, headers=headers)

print(response.text)

