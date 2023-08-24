import time


class DateUtils:

    @staticmethod
    def get_timestamp(ms_flag = False):
        t = time.time()

        ts = int(t)
        if ms_flag:
            ts = ts * 1000

        return ts


    #
    #%Y-%m-%d %H:%M:%S
    #
    @staticmethod
    def get_date_str(ts, formart='%Y%m%d'):
        timeArray = time.localtime(ts)
        return time.strftime(formart, timeArray)



if __name__ == '__main__':
    ts = DateUtils.get_timestamp()
    print(DateUtils.get_date_str(ts))