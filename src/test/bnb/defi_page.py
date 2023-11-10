import json
from fake_useragent import UserAgent
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def sign_in(w, username, pwd):
    ua = UserAgent()
    user_agent = ua.random
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent
    }

    url = 'https://api.de.fi/v1/users/auth/sign-in'
    payload = {
        "emailOrUsername": username,
        "password": pwd
    }

    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    #print('[sign_in]status:', rsp.status_code, ' rsp:', rsp.json())
    return rsp.json()['accessToken']


def claim(w, access_token):
    ua = UserAgent()
    user_agent = ua.random
    headers = {
        'User-Agent': user_agent,
        'Origin':'https://de.fi',
        'Referer':'https://de.fi/',
        'Authorization': 'Bearer ' + access_token
    }

    url = 'https://api.de.fi/v1/gamification/daily-earnings/claim'


    rsp = w.session.request(method='post', url=url, headers=headers)
    print('[claim]status:', rsp.status_code, ' rsp:', rsp.json())



def get_user(w, access_token):
    ua = UserAgent()
    user_agent = ua.random
    headers = {
        'User-Agent': user_agent,
        'Origin': 'https://de.fi',
        'Referer': 'https://de.fi/',
        'Authorization': 'Bearer ' + access_token
    }

    url = 'https://api.de.fi/v1/users'

    rsp = w.session.request(method='get', url=url, headers=headers)
    #print('[get_user]status:', rsp.status_code, ' rsp:', rsp.json())
    return rsp.json()['referralCode']



def add_address(w, access_token, a):
    ua = UserAgent()
    user_agent = ua.random
    headers = {
        'User-Agent': user_agent,
        'Origin': 'https://de.fi',
        'Referer': 'https://de.fi/',
        'Content-Type':'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    url ='https://api.de.fi/v1/users/wallets'

    payload = {
        "address": a.address
    }

    rsp = w.session.request(method='put', url=url, headers=headers, data=json.dumps(payload))
    id = str(rsp.json()['id'])
    msg = 'Please sign if you are owner of: '+a.address+'-' + id
    sig = w.sign_data(a, msg)

    payload = {
        "wallet": a.address,
        "signature": sig
    }
    url = 'https://api.de.fi/v1/users/wallets/validate'
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))

    print('[add_address]status:', rsp.status_code, ' rsp:',rsp.text)
    pass


if __name__ == '__main__':
    w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR)
    records = Wallet.read_wallet_line(file_name='email.csv', file_path_prefix='../../../resource/')[35:36]

    num = 0
    for line in records:
        array = line.split(',')

        username = array[0]
        pwd = array[1].replace('\n', '')

        print('---['+str(num)+']----------username:',username,'pwd:',pwd)
        accessToken = sign_in(w, username, pwd)
        #claim(w, accessToken)
        a1 = Wallet.read_wallet_file('tinc_wallet_1.csv', file_path_prefix='../../../resource/')[:][18]
        #add_address(w, accessToken,a1)
        #invite_code = get_user(w, accessToken)
        #print('invite_url','https://de.fi/claim/?invite=' + invite_code)
        num = num +1
        break
