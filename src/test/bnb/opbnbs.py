from time import sleep

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def mint_opbnbs(w, a1):
    contract_address = a1.address
    gas_gwei = w.w3.from_wei(22000, 'gwei')

    #42.54
    data = '0x646174613a2c7b2270223a226273632d3230222c226f70223a226d696e74222c227469636b223a226f70626e6273222c22616d74223a2231303030227d'
    for i in range(10):
        tx_param = w.build_tx_param(a1, contract_address, gas_gwei=gas_gwei, gas_price_gwei=3, data=data)
        (tx_id, rsp, balance) = w.tx_by_param(a1, tx_param)
        print('tx_id:', tx_id, 'rsp:', rsp['status'])
        sleep(1)


a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, gas_flag=False)

mint_opbnbs(w, a1)