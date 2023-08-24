from src.utils.MysqlPool import mysqlPool


class ProxyDao:

    def query_by_type(self, proxy_type, proxy_flag = '1'):
        columns = ['ip', 'port', 'user_name', 'user_pwd', 'proxy_type', 'proxy_flag', 'proxy_desc','create_time']
        columns_str = ','.join([x for x in columns])
        sql = 'SELECT ' + columns_str + ' FROM b_proxy where proxy_type=\'' + proxy_type + '\' and proxy_flag =' + proxy_flag
        rs = mysqlPool.query(sql)
        return rs

    def delete(self, id):
        sql = 'delete from b_proxy where id=' + id
        return mysqlPool.exeSql(sql)

    def query_count(self, proxy_type, proxy_flag = 1):
        sql = 'select * from b_proxy where proxy_type=\'' + proxy_type + '\' and proxy_flag =' + proxy_flag
        return mysqlPool.queryCount(sql)

    def insert_batch(self, lst):
        sql = 'insert into b_proxy (ip,port,user_name,user_pwd,proxy_type,proxy_flag,proxy_desc,create_time) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        return mysqlPool.insertBatch(sql, lst)

proxyDao = ProxyDao()