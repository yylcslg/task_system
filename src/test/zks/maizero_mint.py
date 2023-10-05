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
    gas_gwei = w.w3.from_wei(940000, 'gwei')
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=0.25, data=data)
    (tx_id, receipt, balance) = w.tx_by_param(a, tx_param)
    print('receipt',receipt)
    if (receipt['status'] == 0):
        print('[address]:', a.address, ' fail......')




a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.ZKS_ERA, gas_flag=False)


mint(w,a1)