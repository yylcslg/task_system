from src.monitor.job_queue import logQueue
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap



def queryDailyInfo(w, address):
    url_2 = 'https://api2.mailzero.network/queryDailyInfo?address=' + address
    rsp = w.session.request(method='get', url=url_2)
    print('[queryDailyInfo] status code:', rsp.status_code, ' content:', rsp.content)


def checkin(w, address):
    url ='https://api2.mailzero.network/checkin?address='+address
    rsp = w.session.request(method='get', url=url)
    print('[checkin] ',address,' status code:' , rsp.status_code, ' content:' , rsp.json())
    return rsp.json()


a1 = account_1
job = job_dict
proxy_ip_str = proxy_ip

w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, proxy_ip=proxy_ip_str, gas_flag=False)
#w = Web3Wrap(block_chain=Block_chain.BSC_ANKR, proxy_ip=proxy_ip_str, gas_flag=False)

#queryDailyInfo(w, a1.address)

rsp =checkin(w, a1.address)

job['tx_receipt']=rsp['status']


# 1:成功 2：失败
if rsp['status'] == 'success':
    job['tx_status'] =1
else:
    job['tx_status'] = 2

#logQueue.queue.put(job)
#https://mailzero.network/stamp?earneth=229068


