#1：mint nft
#2：定时任务功能完善
#2.1：status 设置
#2.2:界面
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def mint(w:Web3Wrap, a):
    data = '0xa0712d680000000000000000000000000000000000000000000000000000000000037ecc'
    contract_address = '0xc94025c2eA9512857BD8E1e611aB9b773b769350'

    amount = float(w.get_balance(a.address, unit='ether'))

    print('address 1:', a.address, 'balance:', amount)




a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.ZKS_ERA, gas_flag=False)


mint(w,a1)