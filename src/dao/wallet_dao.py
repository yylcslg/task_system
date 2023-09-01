from src.utils.MysqlPool import mysqlPool


class WalletDao:

    def select_batch(self, batch_name:str):
        columns = ['wallet_address', 'wallet_key', 'mnemonic', 'batch_name','seq_num','create_date','wallet_desc']
        columns_str = ','.join([x for x in columns])
        sql = 'SELECT ' + columns_str + ' FROM b_wallet where batch_name=\''+batch_name+'\''
        rs = mysqlPool.query(sql)
        return rs

    def select_by_param(self, batch_name: str, start_offset = 0, end_offset=0):
        columns = ['wallet_address', 'wallet_key', 'mnemonic', 'batch_name', 'seq_num', 'create_date', 'wallet_desc']
        columns_str = ','.join([x for x in columns])
        sql = 'SELECT ' + columns_str + ' FROM b_wallet where batch_name=\'' + batch_name + '\' and seq_num >=' +str(start_offset)
        if end_offset > 0 :
            sql = sql + ' and seq_num < ' + str(end_offset)

        rs = mysqlPool.query(sql)
        return rs

    def insert_batch(self, lst):
        sql = 'insert into b_wallet (wallet_address,wallet_key,mnemonic,batch_name,seq_num,create_date,wallet_desc) values(%s,%s,%s,%s,%s,%s,%s)'
        return mysqlPool.insertBatch(sql, lst)


    def delete(self,batch_name):
        sql = 'delete from b_wallet where batch_name=\''+batch_name+'\''
        return mysqlPool.exeSql(sql)

    def select_count(self,batch_name):
        sql = 'select * from b_wallet where batch_name=\''+batch_name+'\''
        return mysqlPool.queryCount(sql)

walletDao = WalletDao()