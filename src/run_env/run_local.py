from src.task_core.task_core_local import TaskCoreLocal
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.test.bnb.defi_page import sign_in, claim, get_user, add_address
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


def run_defi():
    w = Web3Wrap.get_instance(block_chain=Block_chain.Sepolia)
    records = Wallet.read_wallet_line(file_name='email.csv', file_path_prefix='../../resource/')[:]
    #test_account = Wallet.read_test_wallet()
    #tinc_account_1 = Wallet.read_wallet_file('tinc_wallet_1.csv')
    #accounts = test_account + tinc_account_1

    num = 0
    for line in records:
        array = line.split(',')
        username = array[0]
        pwd = array[1].replace('\n', '')
        print('--------------[' + str(num) + ']------------------------------------')
        print('username:', username, 'pwd:...')
        accessToken = sign_in(w, username, pwd)
        #add_address(w, accessToken, accounts[num])
        claim(w, accessToken)
        #invite_code = get_user(w, accessToken)
        #print('invite_url', 'https://de.fi/claim/?invite=' + invite_code)
        num = num + 1


def run_okx_bridge(dir_name, file_name, range_num = 1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[:];tinc_wallet_1[:]'
    #accounts_exp_1 = 'tinc_wallet_1[270:]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 5
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

def run_bnbi(dir_name, file_name, range_num = 1):
    template_txt = read_local_file(dir_name, file_name)
    #accounts_exp_1 = 'test[:];tinc_wallet_1[:]'
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 5
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)


def run_poli(dir_name, file_name, range_num = 1):
    template_txt = read_local_file(dir_name, file_name)
    #accounts_exp_1 = 'test[:];tinc_wallet_1[:]'
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 5
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)


def run_ants(dir_name, file_name, range_num = 1):
    template_txt = read_local_file(dir_name, file_name)
    #accounts_exp_1 = 'test[:];tinc_wallet_1[:]'
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 5
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

def run_ipol(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 8
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

def run_anteater(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[1:2]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)


def run_gors(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

def run_opbnbs(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)


def run_voyage(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)


def run_web3go(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)


def run_starry(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = 'test[0:1]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

def run_send_zeta(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)

    num =0
    gap = 2
    parallelism_num = 1

    for i in range(range_num):
        accounts_exp_1 = 'test[' + str(num) + ':' + str(num + 1) + ']'
        accounts_exp_2 = 'test['+str(num+1)+':'+str(num+2)+']'
        num = num + gap

        TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                                parallelism_num=parallelism_num, db_flag=False)

    pass


def run_zeta_task_1(dir_name, file_name, range_num=1):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:10]'
    accounts_exp_2 = 'test[9:10]'
    parallelism_num = 1
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

    pass


def run_zeta():
    #run_send_zeta('zeta', 'send_zeta.py', 5)
    run_zeta_task_1('zeta', 'zeta_task_1.py')




if __name__ == "__main__":
    #run_zeta()

    run_starry('bnb', 'starry.py')
    run_defi()

    run_mailzero('bnb', 'mailzero.py')


    #run_alienswap('linea', 'alienswap.py')

    #run_unemeta('bnb', 'unemeta.py')
    #run_web3go('bnb','web3go.py')

    #run_okx_bridge('sepolia', 'okx_bridge.py')

    #run_bnbi('bnb', 'bnbi.py')
    #run_poli('pol', 'poli.py')

    #run_ants('pol', 'ants.py')
    #run_ipol('pol', 'ipol.py')
    #run_maizero_mint('zks', 'maizero_mint.py', 1)

    #run_anteater('pol', 'anteater.py')
    #run_gors('goerli', 'gors.py')

    #run_opbnbs('opbnb', 'opbnbs.py')
    #run_voyage('linea', 'voyage.py')
    print("finish...................")
