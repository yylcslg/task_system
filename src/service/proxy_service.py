import time

from src.dao.proxy_dao import proxyDao

class ProxyService:

    def create_proxy(self,ip, port,user_name='', user_pwd='', proxy_type='local_proxy'):
        t = time.time()
        ts = int(t) * 1000
        records = []

        records.append((ip, port, user_name, user_pwd, proxy_type, 1, '', ts))
        proxyDao.insert_batch(records)

    def query_by_type(self, proxy_type):
        rs = proxyDao.query_by_type(proxy_type)
        lst = []
        for line in rs:
            if proxy_type == 'local_proxy':
                lst.append(line['ip'] + ':' + line['port'])
            if proxy_type == 'static_proxy':
                proxy_str = 'http://{0}:{1}@{2}:{3}'.format(line['user_name'],
                                                            line['user_pwd'],
                                                            line['ip'],
                                                            line['port'])
                lst.append(proxy_str)
        #itertools.cycle(lst)
        return lst


if __name__ == '__main__':
    p = ProxyService()
    #p.create_proxy('192.0.0.7','8889', 'yyl','yyl_pwd', 'static_proxy')

    p.query_by_type('static_proxy')
    print('finish.....')