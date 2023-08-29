import time

from src.dao.job_dao import jobDao


class JobService:

    def query_job(self, ts):
        rs = jobDao.query_all(ts)
        return rs


    def modify_job_exe_time(self, job, ts):
        msg_dict = {}
        msg_dict['latest_exe_time'] = ts
        msg_dict['id'] = job['id']
        jobDao.update_job_by_id(msg_dict)
        pass





