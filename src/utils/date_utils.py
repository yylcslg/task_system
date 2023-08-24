import time
import datetime


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

    @staticmethod
    def date_str(day_num=0, format="%Y-%m-%d %H:%M:%S"):
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(days=day_num)
        # 获取想要的日期的时间
        re_date = (today + offset).strftime(format)
        return re_date



if __name__ == '__main__':
    ts = DateUtils.get_timestamp()
    print(DateUtils.get_date_str(ts))