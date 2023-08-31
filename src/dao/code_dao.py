from src.utils.MysqlPool import mysqlPool


class CodeDao:

    def select_by_name(self, code_name):
        columns = ['code_name', 'code_txt', 'accounts_exp_1', 'accounts_exp_2', 'proxy_ip_exp', 'param_exp', 'code_desc']
        columns_str = ','.join([x for x in columns])
        sql = 'SELECT ' + columns_str + ' FROM b_code where code_name=\'' + code_name + '\''
        rs = mysqlPool.query(sql)
        return rs

    def insert_batch(self, lst):
        sql = 'insert into b_code (code_name,code_txt,accounts_exp_1,accounts_exp_2,proxy_ip_exp,param_exp,code_desc) values(%s,%s,%s,%s,%s,%s,%s)'
        return mysqlPool.insertBatch(sql, lst)


    def update_by_id(self, msg_dict):
        id = str(msg_dict['id'])

        columns = []
        for k in msg_dict:
            if k != 'id':
                if isinstance(msg_dict[k], str):
                    columns.append(k + '=\'' + msg_dict[k] + '\'')
                else:
                    columns.append(k + '=' + str(msg_dict[k]))
        columns_str = ','.join([x for x in columns])

        sql = 'update b_code set ' + columns_str + ' where id = ' + id
        mysqlPool.exeSql(sql)

codeDao = CodeDao()