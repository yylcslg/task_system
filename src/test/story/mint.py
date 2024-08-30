from datetime import datetime
import json

from eth_account import Account

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

contract_abi='[{"inputs":[{"internalType":"address","name":"storyProtocolGateway","type":"address"},{"internalType":"address","name":"licenseRegistry","type":"address"},{"internalType":"address","name":"pilTemplate","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ECDSAInvalidSignature","type":"error"},{"inputs":[{"internalType":"uint256","name":"length","type":"uint256"}],"name":"ECDSAInvalidSignatureLength","type":"error"},{"inputs":[{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"ECDSAInvalidSignatureS","type":"error"},{"inputs":[],"name":"EnforcedPause","type":"error"},{"inputs":[],"name":"ExpectedPause","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ip","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"flag","type":"bool"}],"name":"SignatureCheckFlipped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"LICENSE_REGISTRY","outputs":[{"internalType":"contract ILicenseRegistry","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PIL_TEMPLATE","outputs":[{"internalType":"contract IPILicenseTemplate","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SPG","outputs":[{"internalType":"contract IStoryProtocolGateway","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deriativeIPMetadataHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"derivativeIPMetadataURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"flag","type":"bool"}],"name":"flipSkipSignatureCheck","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addressToCheck","type":"address"}],"name":"getHasMinted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"twHash","type":"string"}],"name":"getIsTwitterHashUsed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addressToCheck","type":"address"}],"name":"getMintedTokenId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNFTContract","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getParentIpId","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getParentLicenseTermsId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getParentTokenId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getSkipSignatureCheck","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"hasMinted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"string","name":"twHash","type":"string"}],"name":"mintNFTGated","outputs":[{"internalType":"address","name":"ipId","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"mintedUserToTokenId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nftContract","outputs":[{"internalType":"contract ISPGNFT","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"metadataURI","type":"string"},{"internalType":"bytes32","name":"metadataHash","type":"bytes32"}],"name":"setDerivativeIPMetadata","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_signer","type":"address"}],"name":"setSignerAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"signer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"usedTwHashes","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'


def process():
    w = Web3Wrap(block_chain=Block_chain.Story, gas_flag=False)
    wallet = Wallet()
    rsp = sign(w, wallet)

    print('signature:', rsp['signature'])
    print('twHash:', rsp['hashedTwitterId'])
    #mint(w,wallet,signature='',twHash='')




def sign(w:Web3Wrap, a:Account):
    nonce =nonce_msg(w, a)
    url = 'https://mint.story.foundation/api/mint/signature'
    message = f"mint.story.foundation wants you to sign in with your Ethereum account:\n{a.address}\n\nSign in with Ethereum to the app.\n\nURI: https://mint.story.foundation\nVersion: 1\nChain ID: 1513\nNonce: {nonce}\nIssued At: {get_sign_time()}"
    challengeToken='0.oXCBuHxsniBWftl8k1jb3NTIrc2NAZhblz3RxQrBaUoNDIoVDt_Oh5eNVXISAxL37UstFia_t1SiB07x4wBmpU - hYYIBlUWwf51IM90ow_dEK4aLiXliXtmD - nDURpR7Wd9 - C3Hn1KuvIjmIZMg - BUx - VEnZ6Z0lVTe5Kr20Pny3kO66 - T5APZRARhotCCkvipEgeASSHCbIqhKRmtKkvTxm79bMnNvx88MhhgJZOZC4jA2RtVIvUx2l59f3Q9V9SERH4Ip_36BtXlAllexHoTPqnqivmCGUHmG13f59J5kW - perZIK5ZTzPFs93b06sv6hNrLsz7i_TimUghhZLOkgvFdvTSAW6oFINFVzTAw5YUzy2d3JtmQV6eJ757BG30 - TWMhDy0dFC4N0G10uSxxbOkE74Ja08HvmT0z8ZGo0r15ylnInRfubj4Xmsd7v4. - nDZ4dmSaj14Jl2btrnKIA.54ad7bb7f3d386037aacc7477e5a5575e6422a2fe1bc273d342f975bd7965a79'
    payload = {
        "address": a.address,
        "challengeToken":challengeToken,
        "message": message,
        "signature": w.sign_data(a, message),
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent
    }
    rsp = w.session.request(method='post', url=url, headers=headers, data=json.dumps(payload))

    print('nonce:',nonce)
    print('signature:', w.sign_data(a, message))
    print('rsp:', rsp.json())
    return rsp.json()


#https://challenges.cloudflare.com/turnstile/v0/api.js?onload=${e}&render=explicit
def mint(w:Web3Wrap, wallet:Wallet, signature,twHash):
    file_name='tinc_wallet_1.csv'
    num = 0
    end_num = 1
    other_account = wallet.read_wallet_file(file_name=file_name,
                                            file_path_prefix='../../../resource/')[num:end_num]  # 等待收集的账户

    gas_gwei = w.w3.from_wei(1361328, 'gwei')
    gas_price_gwei = 734.4

    for a in other_account:
        print('------------------------', file_name,'---',num, '--------------------------------------------')

        num = num + 1
        contract_address = '0xFaa402A8bc7C88D252cd4Bc64C154fcB8031d015'  # 合约地址

        tx_param = w.contract_build_tx_param(contract_address=contract_address,
                                             abi=contract_abi,
                                             from_account=a,
                                             gas_gwei=gas_gwei,
                                             gas_price_gwei= gas_price_gwei,
                                             method_name='mintNFTGated',
                                             signature=signature,
                                             twHash=twHash)
        print('tx_param:', tx_param)
        tx_id = w.tx(a, tx_param=tx_param)
        print('tx_id:', tx_id)
        rsp = w.get_receipt(tx_id)
        balance = w.get_balance(a.address, unit='ether')

        print('[status]:', rsp['status'], '[address]:', a.address, ' [balance]:', balance, ' [tx count]:',w.get_tx_count(a.address))
        return (tx_id, rsp, balance)




def nonce_msg(w:Web3Wrap, a:Account):
    url = 'https://mint.story.foundation/api/wallet/nonce'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': user_agent
    }

    payload = {
        "walletAddress": a.address
    }
    rsp = w.session.request(method='post', url=url, headers=headers,data=json.dumps(payload))

    return rsp.json()['nonce']

def get_sign_time():
    # 获取当前时间
    current_time = datetime.utcnow()
    # 格式化时间为 Aug 12 14:14 (UTC+0) 格式
    formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_time



if __name__ == '__main__':
    process()

    print('finish.....')
    pass