from src.utils.MysqlPool import mysqlPool


class JobInstanceDao:


    def insert_job_instance(self, map_list):
        columns = []
        values = []
        for k in map_list[0]:
            columns.append(k)
            values.append('%s')

        lst = []
        for d in map_list:
            temp_lst = []
            for k in d:

                temp_lst.append(d[k])
            t = tuple(temp_lst)
            lst.append(t)

        columns_str = ','.join([x for x in columns])
        values_str = ','.join([x for x in values])
        sql = 'insert into j_job_instance (' +columns_str +') values(' + values_str + ')'

        return mysqlPool.insertBatch(sql, lst)



jobInstanceDao = JobInstanceDao()