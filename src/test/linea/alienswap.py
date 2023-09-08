import json
import time

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def signin(w, a1, invitation_code):

    url = "https://alienswap.xyz/alien-api/api/v1/public/user/signin?network=eth"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        #'Content-Type': 'application/json; charset=utf-8',
        #'Referer':'https://alienswap.xyz/rewards',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'
    }

    sign_text = "Welcome to AlienSwap!\nClick to sign in and accept the AlienSwap Terms of Service.\nThis request will not trigger a blockchain transaction or cost any gas fees."
    sig = w.sign_data(a1, sign_text)
    payload = {
        "address": a1.address,
        "signature": sig,
        "nonce": sign_text,
        "inviter": invitation_code,
        "src": 4,
        "network": "eth"
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    #print('[signin]status:', rsp.status_code, ' rsp:', rsp.content)

    accessToken = rsp.json()['data']['access_token']
    return accessToken


def twitter_box(w, a1, access_token):
    url = 'https://alienswap.xyz/alien-api/api/v1/private/points/account/twitter/verify?network=eth'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + access_token,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    payload = {
        "address": a1.address,
        "network": "eth"
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[twitter_box]status:', rsp.status_code, ' rsp:', rsp.json())


def checkin(w, a1, access_token):
    #url = "https://alienswap.xyz/alien-api/api/v1/private/points/account/others/info?network=eth"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + access_token,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    payload = {
        "address": a1.address,
        "network": "eth"
    }

    #rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    #print('[checkin points]status:', rsp.status_code, ' rsp:', rsp.json())

    #if rsp.json()["data"]["checkin"] == 0:
    print('开始签到')
    url = "https://alienswap.xyz/alien-api/api/v1/private/points/account/checkin/claim?network=eth"
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[checkin]status:', rsp.status_code, ' rsp:', rsp.json())

def points_info(w, a1, access_token):
    url = "https://alienswap.xyz/alien-api/api/v1/private/points/account/info?network=eth"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + access_token,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    payload = {
        "address": a1.address,
        "network": "eth"
    }

    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[points_info]status:', rsp.status_code,' total score:', rsp.json()["data"]["total_points"], ' rsp:', rsp.json())



a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.LINEA, gas_flag=False)

invitation_code = 'd3L9oT'
accessToken = signin(w, a1, invitation_code)
#twitter_box(w, a1, accessToken)

time.sleep(1)
checkin(w, a1, accessToken)
#points_info(w, a1, accessToken)
time.sleep(1)

#https://alienswap.xyz/rewards