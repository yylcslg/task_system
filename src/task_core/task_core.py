from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.tools import msg_decode


class TaskCore:

    def __init__(self, exec_txt):
        self.exec_txt = msg_decode(exec_txt)

    def setup(self):
        #if self.urls == None:
        self.runSingle(self.exec_txt)

        #for url in self.urls.split(","):
            #if self.run_state:self.runSingle(self.exec_txt, url=url, params=self.params)


    def runSingle(self, exec_txt):
        url = ''
        params = ''
        try:
            w = Web3Wrap(block_chain=Block_chain.BSC_ANKR, gas_flag=False)
            exec(exec_txt, {"w": w, "params": params})
        except Exception as e:
            print('error...', e)
        return url


    def stop(self):
        self.run_state = False
        print("stop...")

