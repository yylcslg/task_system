from src.task_core.task_core_local import TaskCoreLocal
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.test.bnb.defi_page import sign_in, claim, get_user
from src.test.save_template_task import p
from src.utils.tools import msg_encode
from src.utils.wallet_account import Wallet


def read_local_file(dir_name, file_name):
    with open(p +dir_name+'/'+ file_name) as f:
        template_txt = msg_encode(f.read())
    return template_txt


def run_mailzero(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[:];tinc_wallet_1[:];tinc_wallet_2[:];tinc_wallet_3[:]'
    #accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = ''
    parallelism_num = 10
    TaskCoreLocal.local_run(template_txt, accounts_exp_1= accounts_exp_1, accounts_exp_2 = accounts_exp_2,
                            parallelism_num = parallelism_num, db_flag= False)


def run_unemeta(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[:];tinc_wallet_1[:];tinc_wallet_2[:];tinc_wallet_3[:];tinc_wallet_4[:]'
    #accounts_exp_1 = 'tinc_wallet_4[:]'
    accounts_exp_2 = ''
    parallelism_num = 10
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag= False)


def run_alienswap(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[:];tinc_wallet_1[:];tinc_wallet_2[:];tinc_wallet_3[:]'
    #accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = ''
    parallelism_num = 3
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag= False)


def run_maizero_mint(dir_name, file_name, range_num = 1):
    template_txt = read_local_file(dir_name, file_name)
    for i in range(range_num):
        accounts_exp_1 = 'test[0:1]'
        #accounts_exp_1 = 'tinc_wallet_3[:]'
        accounts_exp_2 = ''
        parallelism_num = 1
        #print('', template_txt)
        TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                                parallelism_num=parallelism_num, db_flag= False)


def defi_run():
    w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR)

    records = Wallet.read_wallet_line(file_name='email.csv', file_path_prefix='../../resource/')[:]
    num = 0
    for line in records:
        array = line.split(',')
        username = array[0]
        pwd = array[1].replace('\n', '')
        print('--------------[' + str(num) + ']------------------------------------')
        print('username:', username, 'pwd:', pwd)
        accessToken = sign_in(w, username, pwd)
        claim(w, accessToken)
        #invite_code = get_user(w, accessToken)
        #print('invite_url', 'https://de.fi/claim/?invite=' + invite_code)
        num = num + 1




if __name__ == "__main__":

    run_unemeta('bnb', 'unemeta.py')
    run_mailzero('bnb', 'mailzero.py')

    defi_run()

    #run_maizero_mint('zks', 'maizero_mint.py', 1)

    #run_alienswap('linea', 'alienswap.py')

    print("finish...................")