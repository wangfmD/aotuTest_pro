# coding:utf-8
import logging
import sys

def __setlogfile(filepath):
    fh = logging.FileHandler(filepath)
    return fh


def __setstream():
    ch = logging.StreamHandler()
    return ch


def __ststreamstdout():
    cho = logging.StreamHandler(sys.stdout)
    return cho


def init_log(filepath):
    logger = logging.getLogger('CLIENT')
    logger.setLevel(logging.DEBUG)
    fh = __setlogfile(filepath)
    # ch = __setstream()
    cho = __ststreamstdout()
    format = '[%(asctime)s %(name)s %(filename)s line:%(lineno)d %(levelname)s] %(message)s'
    formatstream = '%(message)s'
    formatter = logging.Formatter(format)
    formatterstream = logging.Formatter(formatstream)
    # formatterstreamout = logging.Formatter(formatstream)

    fh.setFormatter(formatter)
    # ch.setFormatter(formatterstream)
    cho.setFormatter(formatterstream)
    logger.addHandler(fh)
    # logger.addHandler(ch)
    logger.addHandler(cho)
    return logger
logging.info('dd')

def T_INFO(logger, msg):
    logger.info(msg)
    print msg




# def init_log(filepath):
#
#     logging.basicConfig(
#         level=logging.INFO,
#         filename=filepath,
#         filemode='w',
#         format='[%(asctime)s %(name)s %(filename)s line:%(lineno)d %(levelname)s] %(message)s'
#     )
#     cho = __ststreamstdout()
#     format = '[%(asctime)s %(name)s %(filename)s line:%(lineno)d %(levelname)s] %(message)s'
#     formatstream = '%(message)s'
#     formatter = logging.Formatter(format)
#     formatterstream = logging.Formatter(formatstream)
#     cho.setFormatter(formatterstream)
#     cho.setLevel(logging.DEBUG)
#     logging.getLogger('').addHandler(cho)
#     return logging

