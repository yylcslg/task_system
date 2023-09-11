import json

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def nonce(w, a1):
    url ='https://www.unemeta.com/api/backend/api/user/v1/users/nonce'
    payload = {"walletAddress": a1.address}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8'
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[nonce]status:', rsp.status_code, ' rsp:', rsp.json())
    return rsp.json()


def resgister(w, a1, nonce_json):
    sig = w.sign_data(a1, nonce_json['data']['noce'])
    print(sig)
    url = 'https://www.unemeta.com/api/backend/api/user/v1/users/resgister'
    payload = {"wallet_address": a1.address,"signData": sig}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8'
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('[resgister]status:', rsp.status_code, ' rsp:', rsp.json())
    return sig


def login(w, a1):
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

def signin(w, a1, accessToken):
    url = 'https://www.unemeta.com/api/backend/api/project/v1/signin?source=2'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization':'Bearer ' +accessToken
    }

    rsp = w.session.request(method='get', url=url, headers=headers)
    print('[signin]status:', rsp.status_code, ' rsp:', rsp.json())



def query_point(w, a1, accessToken):
    url ='https://www.unemeta.com/api/backend/api/integral/v1/uu/info?location=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + accessToken
    }
    rsp = w.session.request(method='get', url=url, headers=headers)
    print('[query_point]status:', rsp.status_code, ' rsp:', rsp.json())



def verifiy_code_method(w, a1, accessToken, verifiy_code):
    url1 = 'https://www.unemeta.com/api/backend/api/project/v1/check/code?is_score_code=1&code='+verifiy_code
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + accessToken
    }
    rsp1 = w.session.request(method='get', url=url1, headers=headers)
    print('[Verifiy_code 1]status:', rsp1.status_code, ' rsp:', rsp1.json())

    url2 = 'https://www.unemeta.com/api/backend/api/project/v1/joinme/scode/succeed?code=' + verifiy_code
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + accessToken
    }
    rsp2 = w.session.request(method='get', url=url2, headers=headers)
    print('[Verifiy_code 2]status:', rsp2.status_code, ' rsp:', rsp2.json())


a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, gas_flag=False)

#nonce_json = nonce(w, a1)
#resgister(w, a1, nonce_json)
accessToken = login(w, a1)
signin(w, a1, accessToken)
#query_point(w, a1, accessToken)


#www.unemeta.com/zh/rewards?invitationCode=true
#eheltl
#verifiy_code ='eheltl'
#verifiy_code_method(w, a1, accessToken, verifiy_code)


#https://www.unemeta.com/zh/rewards

#https://din.web3go.xyz?ref=5a571d41ecada762

