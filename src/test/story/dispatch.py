
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def process():
    w = Web3Wrap(block_chain=Block_chain.Story, gas_flag=False)
    wallet = Wallet()

    dispatch(w,wallet)


def dispatch(w:Web3Wrap, wallet:Wallet):
    start_num =298
    end_num=300
    main_account = wallet.read_wallet_file(file_name='tinc_wallet_1.csv',
                                            file_path_prefix='../../../resource/')[start_num:end_num]  # 等待收集的账户

    other_account_8 = wallet.read_wallet_file(file_name='tinc_wallet_8.csv',
                                           file_path_prefix='../../../resource/')[start_num:end_num]

    other_account_9 = wallet.read_wallet_file(file_name='tinc_wallet_9.csv',
                                              file_path_prefix='../../../resource/')[start_num:end_num]

    other_account_10 = wallet.read_wallet_file(file_name='tinc_wallet_10.csv',
                                              file_path_prefix='../../../resource/')[start_num:end_num]

    num = 0
    gas_gwei = w.w3.from_wei(21000, 'gwei')
    gas_price_gwei = 800
    amount_eth = 2
    for a in main_account:
        print('------------------------   ',start_num, '--------------------------------------------')
        balance = w.get_balance(a.address, unit='ether')
        if (balance>2):

            w.tx_amount(a, other_account_8[num].address, amount_eth, gas_gwei=gas_gwei, gas_price_gwei = gas_price_gwei)
            w.tx_amount(a, other_account_9[num].address, amount_eth, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei)
            w.tx_amount(a, other_account_10[num].address, amount_eth, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei)
            print(main_account[num].address, '  7:', w.get_balance(main_account[num].address, unit='ether'))
            print(other_account_8[num].address, '  8:', w.get_balance(other_account_8[num].address, unit='ether'))
            print(other_account_9[num].address, '  9:', w.get_balance(other_account_9[num].address, unit='ether'))
            print(other_account_10[num].address, '  10:', w.get_balance(other_account_10[num].address, unit='ether'))
            num = num + 1
        start_num =start_num+1









if __name__ == '__main__':
    process()

    print('finish.....')
    pass