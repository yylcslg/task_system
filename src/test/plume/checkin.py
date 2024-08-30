from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
import json
from datetime import datetime
from eth_account import Account


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'


def nonce(w:Web3Wrap, a:Account):
    url = 'https://points-api.plumenetwork.xyz/auth/nonce'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent
    }
    rsp = w.session.request(method='post', url=url, headers=headers)

    return rsp.json()

def sign(w:Web3Wrap, a:Account, nonce,reffer='E0ZR3'):
    message = f"miles.plumenetwork.xyz wants you to sign in with your Ethereum account:\n{a.address}\n\nPlease sign with your account\n\nURI: https://miles.plumenetwork.xyz\nVersion: 1\nChain ID: 161221135\nNonce: {nonce}\nIssued At: {get_sign_time()}"
    url = 'https://points-api.plumenetwork.xyz/authentication'
    payload = {
        "message": message,
        "refferrer": reffer,
        "signature": w.sign_data(a, message),
        "strategy": "web3"
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    access_token = rsp.json()['accessToken']
    print('points:',rsp.json()['user']['totalPoints'])

    return access_token



def checkin(w:Web3Wrap, a:Account):
    contract_address = '0x8Dc5b3f1CcC75604710d9F464e3C5D2dfCAb60d8'
    gas_gwei = w.w3.from_wei(621000, 'gwei')

    # 42.54
    data = '0x183ff085'

    try:

        tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, data=data)
        (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
        print('tx_id:', tx_id, 'rsp:', rsp['status'])
    except Exception as e:
        print('发生错误：{0}'.format(e))

    pass

#https://miles.plumenetwork.xyz/join?invite=PLUME-E0ZR3
def referrer():
    pass



def get_sign_time():
    # 获取当前时间
    current_time = datetime.utcnow()
    # 格式化时间为 Aug 12 14:14 (UTC+0) 格式
    formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_time




a = account_1

w = Web3Wrap.get_instance(block_chain=Block_chain.Plume, gas_flag=False)

checkin(w,a)
nonce = nonce(w, a)
token = sign(w, a,nonce)
#print(token)




