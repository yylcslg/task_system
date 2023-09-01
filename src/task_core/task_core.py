from src.utils.tools import msg_decode


class TaskCore:

    def __init__(self, job_dict={}, template_dict={}, account_exp=''):
        self.job_dict = job_dict
        self.template_dict = template_dict
        self.account_exp = account_exp
        self.run_flag = True


    #1： 创建 job instance 记录， 解析 exp 规则
    #2：获取 account1 所有wallet
    #3：遍历wallet
    #4：记录 执行记录
    #5: 异常处理
    #5.1: 抛出异常3次，任务停止执行 ：每次交易都需要gas， 如果开启重试 ，会导致 亏损
    #5.2 交易 失败状态连续3 次 任务停止
    def run(self):
        print('job_dict:', self.job_dict)
        print('template_dict:', self.template_dict)
        print('account_exp:', self.account_exp)
        proxy_ip_exp = self.template_dict['proxy_ip_exp']


        #if self.urls == None:
        self.runSingle(self.template_txt)

        #for url in self.urls.split(","):
            #if self.run_state:self.runSingle(self.exec_txt, url=url, params=self.params)





    def runSingle(self):
        template_txt = msg_decode(self.template_dict['template_txt'])



    @staticmethod
    def local_run(template_txt):
        try:
            params = ''
            exec(msg_decode(template_txt), {"params": params})
        except Exception as e:
            print('error...', e)

    def stop(self):
        self.run_state = False
        print("stop...")

