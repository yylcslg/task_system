import time
import datetime


class DateUtils:

    @staticmethod
    def get_timestamp(ms_flag = True):
        t = time.time()

        ts = int(t)
        if ms_flag:
            ts = ts * 1000

        return ts


    @staticmethod
    def get_timestamp_min():
        format_str = '%Y-%m-%d %H:%M'
        ts_str = DateUtils.date_str(format = format_str)

        timeArray = time.strptime(ts_str, format_str)

        ts = int(time.mktime(timeArray)) * 1000
        return ts

    #
    #%Y-%m-%d %H:%M:%S
    #
    @staticmethod
    def get_date_str(ts, formart='%Y%m%d'):
        timeArray = time.localtime(ts)
        return time.strftime(formart, timeArray)

    @staticmethod
    def date_str(day_num=0, format ='%Y-%m-%d %H:%M:%S'):
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(days=day_num)
        # 获取想要的日期的时间
        re_date = (today + offset).strftime(format)
        return re_date



if __name__ == '__main__':
    ts = DateUtils.get_timestamp()
    print(DateUtils.date_str(format='%Y%m%d%H%M%S'))