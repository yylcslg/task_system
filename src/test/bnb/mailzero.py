from src.monitor.job_queue import logQueue
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap

a1 = account_1
job = job_dict
proxy_ip_str = proxy_ip

def queryDailyInfo(w, address):
    url_2 = 'https://api.mailzero.network/queryDailyInfo?address=' + address
    rsp = w.session.request(method='get', url=url_2)
    print('[queryDailyInfo] status code:', rsp.status_code, ' content:', rsp.content)


def checkin(w, address):
    url ='https://api.mailzero.network/checkin?address='+address
    rsp = w.session.request(method='get', url=url)
    print('[checkin] ',address,' status code:' , rsp.status_code, ' content:' , rsp.content)


w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, proxy_ip=proxy_ip_str, gas_flag=False)
#w = Web3Wrap(block_chain=Block_chain.BSC_ANKR, proxy_ip=proxy_ip_str, gas_flag=False)

checkin(w, a1.address)
queryDailyInfo(w, a1.address)

job['tx_receipt']='rsp'
logQueue.queue.put(job)


