import time
import  random

from httprunner import __version__
from httprunner.response import ResponseObject


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def get_folders_num(response:ResponseObject):
    print('response===',response.resp_obj.json())
    folders_num = response.resp_obj.json()['data']['folders']
    return len(folders_num)

def gen_random_title():
    return  f"文件-{random.randint(25,80)}"
