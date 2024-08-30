
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def process():
    w = Web3Wrap(block_chain=Block_chain.Sepolia, gas_flag=False)
    wallet = Wallet()
    show_eth(w, wallet)
    #dispatch_eth(w, wallet)
    #sep_bridge_fuel(w, wallet)
    #test(w,wallet)
    #transfer_1_4(w, wallet)



#收集 eth 到主账户
#main_amount 每个钱包最多保留的 eth, 留做gas费用
def show_eth(w:Web3Wrap, wallet:Wallet):
    other_account = wallet.read_wallet_file(file_name='tinc_wallet_2.csv',file_path_prefix='../../../resource/') # 等待收集的账户

    for a in other_account:
        balance = w.get_balance(a.address, unit = 'ether')
        print('address:',a.address,'amount:', balance)


def dispatch_eth(w:Web3Wrap, wallet:Wallet, amount_eth = 0.5, keep_amount = 0.08):
    accounts = wallet.read_test_wallet(file_path_prefix='../../../resource/')
    main_account = accounts[35]  # eth 收集到这个账户
    other_account = wallet.read_wallet_file(file_name='tinc_wallet_3.csv',
                                            file_path_prefix='../../../resource/')[299:] # 等待收集的账户

    gas_gwei = w.w3.from_wei(50000, 'gwei')
    gas_price_gwei = 160
    amount_eth = 0.02
    num = 0
    for a in other_account:
        balance = w.get_balance(a.address, unit = 'ether')
        num = num + 1
        print('------------------------', num, '--------------------------------------------')
        if balance < 0.5:
            w.tx_amount(main_account, a.address, amount_eth, gas_gwei=gas_gwei, gas_price_gwei = gas_price_gwei)
            balance = w.get_balance(a.address, unit='ether')
            print('address:', a.address, 'amount:', balance)



def sep_bridge_fuel(w:Web3Wrap, wallet:Wallet):
    other_account = wallet.read_wallet_file(file_name='tinc_wallet_4.csv',
                                            file_path_prefix='../../../resource/')[1:]  # 等待收集的账户

    lines = wallet.read_wallet_line(file_name='tinc4_fuel_pk.txt',
                                            file_path_prefix='../../../resource/')

    map ={}
    for line in lines:
        array = line.split(",")
        map[array[0]] = array[1][2:].lower().strip()

    #0x1a14e4d4ca64bfcc54708a90f9e2391b6f49ddcf465a50f721dc31d2f4a738e7
    #print(map['0xB326eA9e992Aa3131490aCa54206c38d59c5b23c'])


    gas_gwei = w.w3.from_wei(80000, 'gwei')
    gas_price_gwei = 160
    amount_eth = 0.1

    num = 0
    for a in other_account:
        num = num + 1
        print('------------------------', num, '--------------------------------------------')
        contract_address = '0x01855B78C1f8868DE70e84507ec735983bf262dA'  # 合约地址

        func = '0xd68d9d4e'
        account_address=map[a.address]
        data = func + account_address
        #print(data)
        tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei =gas_price_gwei,data=data, value_eth=amount_eth)
        (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
        #print('tx_id:', tx_id, 'rsp:', rsp['status'])


    pass


def test(w:Web3Wrap, wallet:Wallet):
    lines = wallet.read_wallet_line(file_name='tinc2_fuel_pk.txt',
                                    file_path_prefix='../../../resource/')

    for line in lines:
        array = line.split(",")
        print(array[3].replace("\n",""))


def transfer_1_4(w:Web3Wrap, wallet:Wallet):
    other_account = wallet.read_wallet_file(file_name='tinc_wallet_1.csv',
                                            file_path_prefix='../../../resource/')  # 等待收集的账户

    to_account = wallet.read_wallet_file(file_name='tinc_wallet_4.csv',
                                            file_path_prefix='../../../resource/')[:]

    gas_gwei = w.w3.from_wei(50000, 'gwei')
    gas_price_gwei = 130
    amount_eth = 0.12
    num = 0
    for a in other_account:
        toAddress = to_account[num].address
        balance = w.get_balance(a.address, unit='ether')
        print('------------------------', num, '--------------------------------------------')
        print('address:', a.address, 'amount:', balance, 'toAddress:',toAddress)
        if balance > 0.3:
            w.tx_amount(a, toAddress, amount_eth, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei)
        num = num + 1
        #break

    pass




if __name__ == '__main__':
    process()

    print('finish.....')
    pass