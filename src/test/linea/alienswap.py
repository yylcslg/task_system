import json
import urllib

import requests

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap

# https://alienswap.xyz/rewards?invite_code=d3L9oT

#https://alienswap.xyz/alien-api/api/v1/private/points/account/checkin/claim?network=linea  post
#{"address":"0x7748e319e64c213917a7a2408ee4278f86875d58","network":"linea"}

# Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTM5ODA4NTcsInN1YiI6NzYwMjMxLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1Mjc2ODU3fQ.N6C5bw7SmK0eZvVaNiDcJJuRMuBb4BMAzHbjOli-MN4

w = Web3Wrap.get_instance(block_chain=Block_chain.LINEA, gas_flag=False)

def query_point(w, address='', network=''):
    url = 'https://alienswap.xyz/alien-api/api/v1/private/points/account/info?network=linea'
    payload = {"address":"0x7748e319e64c213917a7a2408ee4278f86875d58","network":"linea"}

    cookie_str = '_ga=GA1.1.2084394760.1685966572; cf_clearance=.vlMA9rvZhO9V7XfshgAhV3CIzn7GcKM_kGQ8wZAoxE-1693980485-0-1-2eed1d16.9037b0a6.79ec42f6-0.2.1693980485; _act=eyIweDMxNDFjY2JjYzM4ZmVjYjM2M2Q1MmYzYTAzZWVjODZjY2RiZTM0ZWIiOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKcFlYUWlPakUyT1RNNU9EQTFNVFVzSW5OMVlpSTZNamsyTlRreExDSjBlWEJsSWpvaVlXTmpaWE56SWl3aVpYaHdJam94TmprMU1qYzJOVEUxZlEuSHlablNlWmN0OHlkMzk3U2wyWnRsMy1KeWlaYnlMWDFHTG1tUXJZRFVDTSIsIjB4Nzc0OGUzMTllNjRjMjEzOTE3YTdhMjQwOGVlNDI3OGY4Njg3NWQ1OCI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpwWVhRaU9qRTJPVE01T0RBNE5UY3NJbk4xWWlJNk56WXdNak14TENKMGVYQmxJam9pWVdOalpYTnpJaXdpWlhod0lqb3hOamsxTWpjMk9EVTNmUS5ONkM1Ync3U21LMGVadlZhTmlEY0pKdVJNdUJiNEJNQXpIYmpPbGktTU40In0=; _ga_7ZE5XDVL6Z=GS1.1.1693980486.3.1.1693983380.0.0.0'
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Authority':'alienswap.xyz',
        'Method': 'POST',
        'Path': '/alien-api/api/v1/private/points/account/info?network=linea',
        'Scheme':'https',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTM5ODA4NTcsInN1YiI6NzYwMjMxLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1Mjc2ODU3fQ.N6C5bw7SmK0eZvVaNiDcJJuRMuBb4BMAzHbjOli-MN4',
        'Content-Length': '74',
        'Content-Type': 'application/json',
        'Cookie': cookie_str,
        'Origin': 'https://alienswap.xyz',
        'Referer': 'https://alienswap.xyz/rewards',
        'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))

    print('[query_point] status code:', rsp.status_code, ' content:', rsp.content)



query_point(w)