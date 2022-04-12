import logging
import logging.handlers
import time
class GetLogger:

    logger = None
    #获取logger
    @classmethod
    def get_logger(cls):

        if cls.logger is None:
            #获取日志器
            cls.logger = logging.getLogger()
            #设置日志器级别
            cls.logger.setLevel(logging.INFO)
            #获取控制台处理器
            sh = logging.StreamHandler()
            #获取文件处理器(时间)
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/{}.log".format(time.strftime("%Y_%m_%d  %H_%M_%S")),
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            #获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            #将格式器添加到处理器
            sh.setFormatter(fmt)
            th.setFormatter(fmt)
            #将处理器添加到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger