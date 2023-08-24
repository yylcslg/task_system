import logging
from logging import handlers


class Web3log:

    def __init__(self, log_name='task_system', log_level = "INFO", max_mb = 10, fomat_str = "%(asctime)s-thread[%(threadName)s]-process[%(process)d]-[%(levelname)s]:%(message)s"):
        log = logging.getLogger(log_name)
        log.setLevel(log_level)
        fh = handlers.RotatingFileHandler(""+log_name + ".log", maxBytes = max_mb*1024*1024, backupCount=100000)
        fh.setLevel(log_level)
        log.addHandler(fh)
        format = logging.Formatter(fomat_str)
        fh.setFormatter(format)

        self.log = log


    def msg_info(self, msg, print_flag:bool = True, *args, **kwargs):
        if print_flag:
            print(msg,*args)
        self.log.info(msg,*args, **kwargs)

    def msg_error(self, msg, print_flag: bool = True, *args, **kwargs):
        if print_flag:
            print(msg,*args)
        self.log.error(msg,*args, **kwargs)

log_info = Web3log(log_name='task_system', log_level = "INFO")
log_error = Web3log(log_name='task_system_error', log_level='ERROR')