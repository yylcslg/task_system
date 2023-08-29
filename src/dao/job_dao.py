from src.utils.MysqlPool import mysqlPool


class JobDao:

    def query_all(self, ts,job_flag='1'):
        columns = ['id', 'job_name', 'job_name_cn', 'code_name', 'code_id', 'param_1', 'param_2', 'job_cycle','job_min','job_hour','job_day','job_week','job_month_day'
            ,'latest_exe_time','next_exe_time','parallelism_num','job_desc','job_flag','create_time','update_time']
        columns_str = ','.join([x for x in columns])

        sql = 'SELECT ' + columns_str + ' FROM j_job where  latest_exe_time < '+str(ts)+' and job_flag =' + job_flag

        rs = mysqlPool.query(sql)
        return rs

    def update_job_by_id(self, msg_dict):
        id =  str(msg_dict['id'])

        columns = []
        for k in msg_dict:
            if k !='id':
                if isinstance(msg_dict[k],str):
                    columns.append(k + '=\'' + msg_dict[k]+'\'')
                else:
                    columns.append(k + '=' + str(msg_dict[k]) )
        columns_str = ','.join([x for x in columns])

        sql ='update j_job set '+ columns_str +' where id = ' + id
        mysqlPool.exeSql(sql)
        pass

jobDao = JobDao()