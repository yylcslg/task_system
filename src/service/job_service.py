from src.dao.job_dao import jobDao
from src.dao.job_instance_dao import jobInstanceDao
from src.utils.date_utils import DateUtils


class JobService:

    def query_job(self, ts):
        rs = jobDao.select_all(ts)
        return rs


    def modify_job_exe_time(self, job, ts):
        msg_dict = {}
        msg_dict['latest_exe_time'] = ts
        msg_dict['id'] = job['id']
        jobDao.update_by_id(msg_dict)


    def save_job_instance(self, t, job_dict):
        account_tuple = t[1]
        job_dict['batch_name'] = account_tuple[0]
        job_dict['batch_from'] = account_tuple[3]
        job_dict['account_total'] = len(t[0])
        ts = DateUtils.get_timestamp()

        lst = []
        instance_dict = {}

        instance_dict['job_id'] = job_dict['id']
        instance_dict['job_name'] = job_dict['job_name']
        instance_dict['job_name_cn'] = job_dict['job_name_cn']
        instance_dict['template_id'] = job_dict['template_id']
        instance_dict['template_name'] = job_dict['template_name']
        instance_dict['instance_id'] = job_dict['instance_id']
        instance_dict['exe_time'] = ts
        instance_dict['wallet_batch_name'] = job_dict['batch_name']
        instance_dict['wallet_batch_from'] = job_dict['batch_from']
        instance_dict['wallet_account_total'] = job_dict['account_total']
        instance_dict['create_time'] = ts

        lst.append(instance_dict)
        jobInstanceDao.insert_job_instance(lst)




jobService = JobService()



