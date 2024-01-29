import json

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap



def web3_nonce(w, a1):
    url = 'https://reiki.web3go.xyz/api/account/web3/web3_nonce'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {"address": a1.address}

    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[login]status:', rsp.status_code, ' rsp:', rsp.json())
    nonce = rsp.json()['nonce']
    print('nonce:', nonce)
    txt ="{\"msg\":\"reiki.web3go.xyz wants you to sign in with your Ethereum account:\\n0x3141CcBCC38FeCB363d52f3a03EEC86cCDBe34eB\\n\\nWelcome to Web3Go! Click to sign in and accept the Web3Go Terms of Service. This request will not trigger any blockchain transaction or cost any gas fees. Your authentication status will reset after 7 days. Wallet address: 0x3141CcBCC38FeCB363d52f3a03EEC86cCDBe34eB Nonce: KlBm2djjEbvTvk25k\\n\\nURI: https://reiki.web3go.xyz\\nVersion: 1\\nChain ID: 56\\nNonce: WZruyaYkn25EjnMHq\\nIssued At: 2024-01-25T03:32:47.668Z\"}"

    return rsp



def web3_challenge(w, a1, rsp):
    url = 'https://reiki.web3go.xyz/api/account/web3/web3_challenge'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8'
    }
    nonce = rsp.json()['nonce']
    challenge = rsp.json()['challenge']
    sig = w.sign_data(a1, challenge)
    print(sig)

    print(challenge)
    payload = {"address": a1.address,
               "challenge": challenge,
               "nonce":nonce,
               "signature":sig
               }


    rsp1 = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[login]status:', rsp1.status_code, ' rsp:', rsp1.json())



def login(w, a1, rsp):
    url = 'https://www.unemeta.com/api/backend/api/user/v1/users/login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {"wallet_address": a1.address,"sign_data": ""}

    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[login]status:', rsp.status_code, ' rsp:', rsp.json())
    accessToken = rsp.json()['data']['accessToken']
    return accessToken


a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, gas_flag=False)

rsp = web3_nonce(w, a1)

web3_challenge(w, a1, rsp)
#accessToken = login(w, a1)









#https://din.web3go.xyz/api/checkin?day=2023-09-08
#
#
