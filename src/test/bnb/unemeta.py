import json

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap

w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, gas_flag=False)

def query_point(w, address='', network=''):
    url ='https://www.unemeta.com/api/backend/api/integral/v1/uu/info?location=0'

    cookie_str = '_ga=GA1.1.650657755.1693911251; UserWalletAddress=0x3141CcBCC38FeCB363d52f3a03EEC86cCDBe34eB; Authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50S2V5IjoiIiwiY2VudHJhbEVtYWlsIjoiIiwiY2VudHJhbElkIjowLCJleHAiOjE2OTM5OTc2NzYsImlhdCI6MTY5MzkxMTI3Niwiand0VXNlcklkIjo2OTU3NCwid2FsbGV0QWRkcmVzcyI6IjB4MzE0MUNjQkNDMzhGZUNCMzYzZDUyZjNhMDNFRUM4NmNDREJlMzRlQiJ9.wac1PifETAbwHxfBLDqDp10rFo2EQV8u771A1OMr3vw;'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Authority': 'www.unemeta.com',
        'Method': 'GET',
        'Path': '/api/backend/api/integral/v1/uu/info?location=0',
        'Scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50S2V5IjoiIiwiY2VudHJhbEVtYWlsIjoiIiwiY2VudHJhbElkIjowLCJleHAiOjE2OTM5OTc2NzYsImlhdCI6MTY5MzkxMTI3Niwiand0VXNlcklkIjo2OTU3NCwid2FsbGV0QWRkcmVzcyI6IjB4MzE0MUNjQkNDMzhGZUNCMzYzZDUyZjNhMDNFRUM4NmNDREJlMzRlQiJ9.wac1PifETAbwHxfBLDqDp10rFo2EQV8u771A1OMr3vw',
        #'Content-Length': '74',
        'Content-Type': 'application/json; charset=utf-8',
        'Cookie': cookie_str,
        'Nextlocale': 'zh',
        #'Origin': 'https://alienswap.xyz',
        'Referer': 'https://www.unemeta.com/zh/rewards',
        'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    rsp = w.session.request(method='get', url=url, headers=headers)

    print('[query_point] status code:', rsp.status_code, ' encoding:', rsp.encoding,' content:', rsp.content)
    pass



#www.unemeta.com/zh/rewards?invitationCode=true
#eheltl
#
#



#{"code":200,"msg":"OK","data":{"noce":"Welcome to Unemeta!\nThis request will not trigger a blockchain transaction or cost any gas fees.\n\nYour authentication status will reset after 24 hours.\n  \nWallet address:\n0x1Ee62353F811fB4C78F05fF7f3bF09BE4DaEa6c8       \nNonce:\n1693989496"}}


#https://www.unemeta.com/api/backend/api/user/v1/users/resgister
# {
#   "wallet_address": "0x1Ee62353F811fB4C78F05fF7f3bF09BE4DaEa6c8",
#   "signData": "0x8913dbdbd83c8bc88c482e2cf4206c4696a54de05019f863dfbf0a14aecddb164112326289eaea5f199ce1ecc8e5eea35e79e04dbc337557b89b2cc56cdf63781b"
# }

#https://www.unemeta.com/api/backend/api/user/v1/users/login
#{
#  "wallet_address": "0x1Ee62353F811fB4C78F05fF7f3bF09BE4DaEa6c8",
#  "sign_data": ""
#}
#
#{"code":200,"msg":"OK","data":{"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50S2V5IjoiIiwiY2VudHJhbEVtYWlsIjoiIiwiY2VudHJhbElkIjowLCJleHAiOjE2OTQwNzU5MDMsImlhdCI6MTY5Mzk4OTUwMywiand0VXNlcklkIjo3MDE5OSwid2FsbGV0QWRkcmVzcyI6IjB4MUVlNjIzNTNGODExZkI0Qzc4RjA1ZkY3ZjNiRjA5QkU0RGFFYTZjOCJ9.llw6fNVYzW2ugeI5JwBtFpSpPADLEgGLt7F8Ylh0vK0","accessExpire":1694162303,"refreshAfter":1694075903}}
a1 = account_1


#https://www.unemeta.com/api/backend/api/user/v1/users/nonce
#{
#  "walletAddress": "0x1Ee62353F811fB4C78F05fF7f3bF09BE4DaEa6c8"
#}
def nonce(w, a1):
    url ='https://www.unemeta.com/api/backend/api/user/v1/users/nonce'
    payload = {"walletAddress": a1.address}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8'
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))
    print('status:', rsp.status_code, ' rsp:', rsp.json())



nonce(w, a1)


#content = {"code":200,"msg":"OK","data":{"noce":"Welcome to Unemeta!\nThis request will not trigger a blockchain transaction or cost any gas fees.\n\nYour authentication status will reset after 24 hours.\n  \nWallet address:\n0x1Ee62353F811fB4C78F05fF7f3bF09BE4DaEa6c8       \nNonce:\n1693989496"}}
#sig = w.sign_data(a1,content['data']['noce'])
#print(sig)
