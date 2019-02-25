"""
    Web_server添加配置文件,conf文件里面是类似字典的字符串，通过eval()就能把字符串转为python对应的数据类型-字典

    conf配置文件中可以设置一些**固定**的资源：框架路径，服务器端口号等等

    shell脚本来配置运行服务器，不需要自己手动输入文件名+运行时参数
    shell脚本中是一些linux命令(能够在linux终端运行的命令)，在**权限允许**的情况下，会从头到尾执行一遍
    shell脚本一般用来运维和自动部署：同时更新100台电脑
    在lunux系统下通过：chmod u+x run.sh 添加X的权限，使其能够直接通过./run.sh来运行
"""

import logging


def test01():

    """logging日志，可以用来记录用户不同页面的浏览顺序，用来分析用户喜好"""

    # logging的配置只需要被设置一次，5个级别，从低到高
    # DEGUB     调试
    # INFO      普通信息
    # WARNING   警告：发送短信次数还剩100次
    # ERROR     错误信息
    # CRITICAL  很严重的bug:磁盘写入快要满了

    # 这里logging的level是warning，只有级别 >=warning的时候，才会在终端输出
    logging.basicConfig(level=logging.WARNING,
                        filename="./log.txt",       # 设置写到文件，不在终端输出
                        filemode="w",
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    # 开始使用log功能
    logging.debug('这是 loggging debug message')
    logging.info('这是 loggging info message')
    logging.warning('这是 loggging a warning message')
    logging.error('这是 an loggging error message')
    logging.critical('这是 loggging critical message')

    # asctime                   filename   lineno     levelname     message
    # 2019-02-25 20:15:40,053 - basic02.py[line:24] - WARNING: 这是 loggging a warning message
    # 2019-02-25 20:15:40,053 - basic02.py[line:25] - ERROR: 这是 an loggging error message
    # 2019-02-25 20:15:40,053 - basic02.py[line:26] - CRITICAL: 这是 loggging critical message


def test02():

    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关，不能低于这个低级，文件中的是debug，但是会无效，取决于总开关的级别

    # 第二步，创建一个handler，用于写入日志文件
    logfile = './log.txt'
    fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关

    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第五步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 日志
    logger.debug('这是 logger debug message')
    logger.info('这是 logger info message')
    logger.warning('这是 logger warning message')
    logger.error('这是 logger error message')
    logger.critical('这是 logger critical message')


def main():

    test01()        # 日志输出到终端或者文件
    test02()        # 日志通过logger对象，分别设置各个权限输出终端和文件


if __name__ == '__main__':
    main()