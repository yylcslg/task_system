from time import sleep

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def process():
    w = Web3Wrap(block_chain=Block_chain.TAIKO_TEST, gas_flag=False)

    dispatch_tx(w)
    #mint_taiko_entry_pass(w)
    #mint_taiko_blazpay(w)

    #setApprovalForAll(w)


def dispatch_tx(w:Web3Wrap):
    print('--------------------------dispatch_tx-------------------------------------------')
    accounts = Wallet.read_test_wallet(file_path_prefix='../../../resource/')
    main_account = accounts[0]
    other_account = Wallet.read_wallet_file('tinc_wallet_1.csv',file_path_prefix='../../../resource/')[25:]
    gas_gwei = w.w3.from_wei(320000, 'gwei')
    gas_price_gwei = 0.00000001
    amount_eth = 0.0004
    for a in other_account:
        try:
            w.tx_amount(main_account, a.address, amount_eth, gas_gwei=gas_gwei, gas_price_gwei = gas_price_gwei)
        except Exception as e:
            sleep(3)
            print('发生错误：{0}'.format(e))



def mint_taiko_entry_pass(w:Web3Wrap):
    print('--------------------------mint_taiko_entry_pass-------------------------------------------')
    other_account = Wallet.read_wallet_file('tinc_wallet_1.csv',file_path_prefix='../../../resource/')

    contract_address = '0x5aB420bd468BcdCa2660469cfd2AA684B6f9a0dc'  # 合约地址

    gas_gwei = w.w3.from_wei(320000, 'gwei')
    gas_price_gwei = 0.000000004
    for a in other_account:
        try:
            data = '0x40d097c3' + w.hex_zfill(a.address).lower()
            tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei,data=data)
            (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
            print('tx_id:', tx_id, 'rsp:', rsp['status'])
        except Exception as e:
            sleep(3)
            print('发生错误：{0}'.format(e))


def mint_taiko_blazpay(w:Web3Wrap):
    print('--------------------------mint_taiko_blazpay-------------------------------------------')
    other_account = Wallet.read_wallet_file('tinc_wallet_1.csv',file_path_prefix='../../../resource/')

    contract_address = '0xedd0dDaEdbc3FBf67aC4ff2ee14Ace669821eac1'  # 合约地址

    gas_gwei = w.w3.from_wei(320000, 'gwei')
    gas_price_gwei = 0.000000004
    for a in other_account:
        try:
            data = '0x40d097c3' + w.hex_zfill(a.address).lower()
            tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei,data=data)
            (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
            print('tx_id:', tx_id, 'rsp:', rsp['status'])
        except Exception as e:
            sleep(3)
            print('发生错误：{0}'.format(e))



def setApprovalForAll(w:Web3Wrap):
    print('--------------------------setApprovalForAll-------------------------------------------')
    other_account = Wallet.read_wallet_file('tinc_wallet_1.csv',file_path_prefix='../../../resource/')

    contract_address = '0xedd0dDaEdbc3FBf67aC4ff2ee14Ace669821eac1'  # 合约地址

    gas_gwei = w.w3.from_wei(50000, 'gwei')
    gas_price_gwei = 0.000000004
    for a in other_account:
        try:
            data = '0xa22cb46500000000000000000000000016700800000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000001'
            tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei, data=data)
            (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
            print('tx_id:', tx_id, 'rsp:', rsp['status'])
        except Exception as e:
            sleep(3)
            print('发生错误：{0}'.format(e))



if __name__ == '__main__':
    process()
    print('finish.....')
    pass