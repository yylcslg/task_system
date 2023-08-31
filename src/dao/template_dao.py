from src.utils.MysqlPool import mysqlPool


class TemplateDao:

    def select_by_name(self, template_name):
        columns = ['template_name', 'template_txt', 'accounts_exp_1', 'accounts_exp_2', 'proxy_ip_exp', 'param_exp', 'template_desc']
        columns_str = ','.join([x for x in columns])
        sql = 'SELECT ' + columns_str + ' FROM b_template where template_name=\'' + template_name + '\''
        rs = mysqlPool.query(sql)
        return rs

    def insert_batch(self, lst):
        sql = 'insert into b_template (template_name,template_txt,accounts_exp_1,accounts_exp_2,proxy_ip_exp,param_exp,template_desc) values(%s,%s,%s,%s,%s,%s,%s)'
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

        sql = 'update b_template set ' + columns_str + ' where id = ' + id
        mysqlPool.exeSql(sql)

templateDao = TemplateDao()