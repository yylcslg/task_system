from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
import json
from datetime import datetime
from eth_account import Account


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'


def sign(w:Web3Wrap, a:Account):
    message = f"You're signing into Infinity AI using your wallet on time: {get_sign_time()}"
    url = 'https://api.infinityai.network/api/v1/sign'
    payload = {
        "from": a.address,
        "hex": w.sign_data(a, message),
        "msg": message,
        "signType": "evm"
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    access_token = rsp.json()['data']['accessToken']

    return access_token

def checkin(w:Web3Wrap, token):
    url = 'https://api.infinityai.network/api/v1/reward/checkIn'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent,
        'Token': token
    }
    rsp = w.session.request(method='post', url=url, headers=headers)
    status = rsp.json()['status']
    if status == 200:
        print(a.address +'... checkin success.....')
    else:
        print(a.address + ' status:' + rsp.json())
    pass

def get_sign_time():
    # 获取当前时间
    current_time = datetime.utcnow()
    # 格式化时间为 Aug 12 14:14 (UTC+0) 格式
    formatted_time = current_time.strftime("%b %d %H:%M (UTC+0)")
    return formatted_time


def refer():
    pass



a = account_1

w = Web3Wrap.get_instance(block_chain=Block_chain.Sepolia, gas_flag=False)
token = sign(w, a)
checkin(w, token)


#print('fractal faucet finish.....')

