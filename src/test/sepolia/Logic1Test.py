from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def f1(w, accounts):
    contract_address = '0xe6a77ff406794b9374ca9bfc032a553486ed3727'
    data = '0xc27fc305'
    num = 0
    for a in accounts:
        print('-----------------------------', num, ' f1 in-----------------------------')
        num = num + 1
        gas_gwei = w.w3.from_wei(2000705, 'gwei')
        tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=16, data=data)
        print(tx_param)
        (tx_id, receipt, balance) = w.tx_by_param(a, tx_param)
        if (receipt['status'] == 0):
            print('[address]:', a.address, ' fail......')
        break


def batch_f1(w,accounts):
    pass

w = Web3Wrap.get_instance(block_chain=Block_chain.Sepolia, gas_flag=False)
accounts = Wallet.read_wallet_file(file_name='mnemonic_wallet_1.csv', file_path_prefix='../../../resource/')[6:10]
f1(w, accounts)
