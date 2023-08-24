from src.dao.wallet_dao import WalletDao
from src.utils.MysqlDB import mysql


def test_sql():
    columns = ['user_name', 'user_pwd', 'user_desc', 'user_flag']
    columns_str = ','.join([x for x in columns])
    sql = 'SELECT ' + columns_str + ' FROM b_user_info'

    # sql = "insert into b_user_info(user_name,user_pwd,user_desc, user_flag) VALUES('test_11','test_1_pwd','test_1_desc',1)"
    # sql = 'delete from b_user_info where id =2'

    # sql = "update b_user_info set user_name = 'tes001' where id =1"
    rs = mysql.query(sql)
    print(rs)


def test_query_wallet():
    wallet =WalletDao()
    rs = wallet.queryByBatch('ba')
    print('rs:',rs)



if __name__ == '__main__':
    #test_sql()
    test_query_wallet()
    print('finish.....')
    pass