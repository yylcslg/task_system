from src.service.job_service import jobService


class JobLog:

    @staticmethod
    def job_log(job_dict, rsp_dict, local_flag = False):

        if local_flag == False:
            jobService.save_job_instance_detail()
        pass