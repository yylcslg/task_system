from src.dao.wallet_dao import walletDao
from src.utils.Properties import pro
from src.utils.date_utils import DateUtils
from src.utils.decode_hex import Decode_hex

from src.utils.wallet_account import Wallet


class WalletService:

    def create_wallet_batch(self, batch_name, total_num = 10):
        count = walletDao.query_count(batch_name)
        if count >0:
            print('batch_name:',batch_name ,' is already exict.....')
            return
        lst = Wallet.create_prefix_address(num=total_num)
        records = self.build_save_batch(lst, batch_name)
        walletDao.insert_batch(records)
        Wallet.save_wallet_file(batch_name +'.csv', lst)


    def query_wallet_by_batch(self, batch_name):
        key = pro.get('aes_key')
        rs = walletDao.query_batch(batch_name)

        for dic in rs:
            dic['wallet_key'] = Decode_hex.decode_aes(key, dic['wallet_key'])
            dic['mnemonic'] = Decode_hex.decode_aes(key, dic['mnemonic'])

        return rs


    def delete_by_batch(self, batch_name):
        return walletDao.delete(batch_name)


    def build_save_batch(self,lines, batch_name, encode_flag = True):
        key = pro.get('aes_key')
        ts = DateUtils.get_timestamp()
        num = 0
        records = []
        for line in lines:
            wallet_address = line[0]
            wallet_key = line[1]
            if encode_flag:
                wallet_key = Decode_hex.encode_aes(key, line[1])

            mnemonic = line[2]
            if encode_flag:
                mnemonic = Decode_hex.encode_aes(key, line[2])
            seq_num = num
            create_date = ts
            records.append((wallet_address, wallet_key, mnemonic, batch_name, seq_num, create_date, ''))
            num = num + 1
        return records


    def import_wallet_from_file(self, lines, batch_name):
        count = walletDao.query_count(batch_name)
        if count > 0:
            print('batch_name:', batch_name, ' is already exict.....')
            return

        records = self.build_save_batch(lines, batch_name)
        walletDao.insert_batch(records)



def read_file():
    w = WalletService()
    lines = Wallet.read_wallet_records('a.csv')
    w.import_wallet_from_file(lines,'batch_2')

if __name__ == '__main__':
    w = WalletService()
    #w.create_wallet_batch('test_3')
    #rs = w.delete_by_batch(batch_name = 'batch_1')
    columns = ['ip', 'port', 'user_name', 'user_pwd', 'proxy_type', 'proxy_flag', 'proxy_desc', 'create_time']
    columns_str = ','.join([x for x in columns])
    print(columns_str)
    #read_file()
    print('finish.....')
    pass