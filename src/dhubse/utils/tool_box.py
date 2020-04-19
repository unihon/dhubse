import sys
import requests
from datetime import datetime


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_ts = datetime.now()
        func(*args, **kwargs)
        print('\nUsed: {}s\n'.format((datetime.now()-start_ts).total_seconds()))

    return wrapper


def req_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            assert res.status_code != requests.codes.not_found, ERROR_MSG['status_code_404']
            assert res.status_code == requests.codes.ok, ERROR_MSG['status_code_not_200']
            return res.json(), res
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
            AssertionError
        ) as e:
            print(str(e))
            sys.exit()

    return wrapper


def color_str(strs, color='green'):
    color_dict = {
        'green': '32m',
        'cyan': '36m'
    }
    res_strs = '\033['+color_dict[color]+strs+'\033[0m'
    return res_strs


def localize_time(isotime):
    tag_time_format = '%Y-%m-%dT%H:%M:%S.%fZ%z'
    f_tag_time_format = '%Y-%m-%dT%H:%M:%S%z'

    datetime_obj = datetime.strptime(
        isotime+'+0000', tag_time_format)
    return datetime_obj.astimezone().strftime(f_tag_time_format)
