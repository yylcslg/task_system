import json
import time

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from fake_useragent import UserAgent


def challenge(w, a1):
    ua = UserAgent()
    user_agent = ua.random

    url = "https://alienswap.xyz/alien-api/api/v1/public/user/sign/challenge?network=scroll"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': user_agent
    }

    addr = w.get_checksum_address(a1.address)
    payload = {
        "address": addr,
        "network": "scroll"
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[challenge]status:', rsp.status_code, ' rsp:', rsp.content)

    message = rsp.json()['data']['message']
    return message

def signin(w, a1, invitation_code, sign_text):
    ua = UserAgent()
    user_agent = ua.random

    url = "https://alienswap.xyz/alien-api/api/v1/public/user/signin?network=scroll"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent':user_agent
    }
    sig = w.sign_data(a1, sign_text)
    payload = {
        "address": a1.address,
        "signature": sig,
        "message": sign_text,
        "inviter": invitation_code,
        "src": 4,
        "network": "scroll"
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[signin]status:', rsp.status_code, ' rsp:', rsp.content)

    accessToken = rsp.json()['data']['access_token']
    return accessToken


def twitter_box(w, a1, access_token):
    url = 'https://alienswap.xyz/alien-api/api/v1/private/points/account/twitter/verify?network=scroll'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + access_token,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    payload = {
        "address": a1.address,
        "network": "scroll"
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
        "network": "scroll"
    }

    #rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    #print('[checkin points]status:', rsp.status_code, ' rsp:', rsp.json())

    #if rsp.json()["data"]["checkin"] == 0:
    print('开始签到')
    url = "https://alienswap.xyz/alien-api/api/v1/private/points/account/checkin/claim?network=scroll"
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


def mint_token2049(w, a1, access_token):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Authorization': 'Bearer ' + access_token
    }

    url = "https://alienswap.xyz/alien-api/api/v1/private/activity/token2049/account/mint?network=eth"
    payload = {
        "partner_uuid": "gDgt2BBJ785S2zqtv5aREn",
        "network": "eth"
    }

    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[mint_token2049]status:', rsp.status_code, ' rsp:',rsp.json())


# https://alienswap.xyz/alien-api/api/v1/public/activity/token2049/user/info?network=base
#{
#  "network": "base"
#}
def mint_2049_info(w, a1, access_token):
    ua = UserAgent()
    user_agent = ua.random
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': user_agent,
        'Authorization': 'Bearer ' + access_token
    }

    url = "https://alienswap.xyz/alien-api/api/v1/public/activity/token2049/user/info?network=eth"
    payload = {
        "network": "eth"
    }

    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[mint_2049_info]status:', rsp.status_code, ' rsp:', rsp.json())

a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.LINEA, gas_flag=False)
message = challenge(w, a1)
invitation_code = 'd3L9oT'
accessToken = signin(w, a1, invitation_code, message)
#twitter_box(w, a1, accessToken)

time.sleep(1)
checkin(w, a1, accessToken)

#mint_token2049(w, a1, accessToken)

#points_info(w, a1, accessToken)
#mint_2049_info(w, a1, accessToken)
time.sleep(1)

#https://alienswap.xyz/rewards