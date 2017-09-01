"""
author: Mookeun Ji, goofcode@gmail.com
"""

import json

from selenium import webdriver
from exception import NoSuchDriverException


def url_join(main_url, sub_url):
    """
    :param main_url: main url that specify host and sub directory
    :param sub_url: sub directory url to be concatenated to main_url
    :return: concatenated url
    """
    if main_url[-1] is '/' and sub_url[0] is '/':
        return main_url[0:-1] + sub_url
    elif main_url[-1] is not '/' and sub_url[0] is not '/':
        return main_url + '/' + sub_url
    else:
        return main_url + sub_url


def get_driver(mode='phantom'):
    """
    :param mode: run mode('chrome' or 'phantom')
    :exception  raise NoSuchDriverException if mode is incorrect
    :return: new web selenium driver
    """
    if mode is 'chrome':
        driver = webdriver.Chrome(get_setting()['chrome_driver_path'])
    elif mode is 'phantom':
        driver = webdriver.PhantomJS(get_setting()['phantom_driver_path'])
    else:
        raise NoSuchDriverException('mode should be either "chrome" or "phantom"')

    driver.implicitly_wait(1)
    return driver


def get_setting():
    """
    get setting specified in setting.json
    :return: dictionary that contains setting
    """

    with open('setting.json', 'r') as setting:
        return json.load(setting)


def get_kakao_data():
    """
    get kakao web info from kakao.json
    :return: dictionary that contains kakao web info
    """

    with open('kakao.json', 'r', encoding='utf-8') as kakao_data:
        return json.load(kakao_data)


