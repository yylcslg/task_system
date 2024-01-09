from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


#https://app.zpet.tech/api/airdrop/eligibility/0xb326ea9e992aa3131490aca54206c38d59c5b23c

def mint(w:Web3Wrap, a):
    url ='https://app.zpet.tech/api/airdrop/eligibility/' + a.address

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    rsp = w.session.request(method='get', url=url, headers=headers)

    print(a.address, rsp.content)

    pass

w = Web3Wrap.get_instance(block_chain=Block_chain.ZKS_ERA, gas_flag=False)

accounts = Wallet().read_test_wallet(file_path_prefix='../../../resource/')
for a in accounts:
    mint(w,a)