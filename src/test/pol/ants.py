from time import sleep

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def mint_ants(w, a1):
    contract_address = a1.address
    gas_gwei = w.w3.from_wei(25000, 'gwei')

    #42.54
    data = '0x646174613a2c7b2270223a227072632d3230222c226f70223a226d696e74222c227469636b223a22616e7473222c22616d74223a22313030303030303030227d'

    for i in range(1000):
        print('----------num:'+str(i)+'--------------------')
        tx_param = w.build_tx_param(a1, contract_address, gas_gwei=gas_gwei, gas_price_gwei=90, data=data)
        (tx_id, rsp, balance) = w.tx_by_param(a1, tx_param)
        print('tx_id:', tx_id, 'rsp:', rsp['status'])
        sleep(2)



a1 = account_1
w = Web3Wrap(block_chain=Block_chain.POLYGON, gas_flag=False)

mint_ants(w, a1)