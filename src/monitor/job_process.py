from src.monitor.job_queue import jobQueue
from src.utils.log import log_error
from src.utils.threads.job_thread_pool import job_process_thread


class JobProcess:

    def process(self):
        while True:
            try:
                j = jobQueue.queue.get()
                job_process_thread.submit(self.multi_process, j)
                #time.sleep(1)
            except Exception as e:
                print('error:', e)
                #log_error.msg_error('error', e)


    def multi_process(self, job):
        parallelism_num = job['parallelism_num']
        if parallelism_num > 1:
            pass

        print('new process job:', job)
        pass

jobProcess = JobProcess()
