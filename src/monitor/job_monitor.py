import time

from src.monitor.job_queue import jobQueue
from src.service.job_service import JobService
from src.utils.date_utils import DateUtils
from src.utils.log import log_error


class JobMonitor:
    job = JobService()

    def monitor_job(self):
        while(True):
            try:
                ts = DateUtils.get_timestamp_min()
                rs = self.job.query_job(ts)
                filter_rs = self.filter_enable_job(rs)
                if len(filter_rs) > 0:
                    for j in filter_rs:
                        j['instance_id'] = ts
                        self.job.modify_job_exe_time(j, ts)
                        jobQueue.queue.put(j)
                        print('put after size:', jobQueue.queue.qsize())

                time.sleep(40)
            except Exception as e:
                print('error:', e)
                log_error.msg_error('error', e)



    def filter_enable_job(self, rs):

        return rs


if __name__ == '__main__':
    j = JobMonitor()
    j.monitor_job()