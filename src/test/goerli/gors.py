from time import sleep

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def mint_goerli(w, a1):
    contract_address = a1.address
    gas_gwei = w.w3.from_wei(32868, 'gwei')

    #42.54
    data = '0x646174613a2c7b2270223a226772632d3230222c226f70223a226d696e74222c227469636b223a22676f7273222c22616d74223a223130227d'

    for i in range(20):
        try:
            print('----------num:'+str(i)+'--------------------')
            tx_param = w.build_tx_param(a1, contract_address, gas_gwei=gas_gwei, gas_price_gwei=15627, data=data)
            (tx_id, rsp, balance) = w.tx_by_param(a1, tx_param)
            print('tx_id:', tx_id, 'rsp:', rsp['status'])
            sleep(1)
        except Exception as e:
            sleep(10)
            print('发生错误：{0}'.format(e))

def echo_goerli(w, a1):
    ontract_address = a1.address
    gas_gwei = w.w3.from_wei(25000, 'gwei')
    print(w.get_balance(a1.address,unit = 'ether'))



a1 = account_1
w = Web3Wrap(block_chain=Block_chain.GOERLI_TEST, gas_flag=False)

mint_goerli(w, a1)


