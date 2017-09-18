"""
author: Mookeun Ji, goofcode@gmail.com
"""

import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .exception import *

DEV = False
current_dir = os.path.dirname(os.path.abspath(__file__))

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

def get_settings():
    if DEV:
        with open(os.path.join(current_dir, 'dev_setting.json'), 'r') as settings_json:
            return json.load(settings_json)
    else:
        with open(os.path.join(current_dir, 'setting.json'), 'r') as settings_json:
            return json.load(settings_json)

def get_locators():
    with open(os.path.join(current_dir, 'locator.json'), 'r', encoding='utf-8') as locators_json:
        return json.load(locators_json)

def get_settings_and_locators():
    """
    get setting and locators specified in setting.json
    :return: 2 dictionaries that contains setting and locators
    """
    return get_settings(), get_locators()



# utils for crawling
def get_driver(mode='phantom'):
    """
    :param mode: run mode('chrome' or 'phantom')
    :exception  raise NoSuchDriverException if mode is incorrect
    :return: new web selenium driver
    """
    if mode is 'chrome':
        driver = webdriver.Chrome(get_settings()['chrome_driver_path'])
    elif mode is 'phantom':
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/60.0.3112.113 Safari/537.36')

        driver = webdriver.PhantomJS(executable_path=get_settings()['phantom_driver_path'],
                                     desired_capabilities=dcap,
                                     service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
        driver.set_window_size(1920, 1080)
    else:
        raise NoSuchDriverException()

    return driver

def wait_until_load(driver, by, locator, timeout=30):
    """
    :param driver: selenium driver loading page
    :param by: locating method 'id', 'xpath', 'class'
    :param locator: proper locator according to param by
    :param timeout: maximum time to wait. After this time elapsed, TimeoutException will be raised.
    :return: web element object waiting for
    """
    if by is 'id':
        return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((By.ID, locator)))
    elif by is 'xpath':
        return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((By.XPATH, locator)))
    elif by is 'class':
        return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((By.CLASS_NAME, locator)))
    else:
        raise NoSuchLocateMethodException()



def login_pf_center(driver):
    settings, locators = get_settings_and_locators()
    to_login_page(driver)
    wait_until_load(driver, 'id', locators['login_email_input_id']).send_keys(settings['admin_info']['email'])
    wait_until_load(driver, 'id', locators['login_pw_input_id']).send_keys(settings['admin_info']['pw'])
    wait_until_load(driver, 'id', locators['login_submit_btn_id']).click()
    return driver

def to_login_page(driver):
    driver.get(get_locators()['pf_login_url'])

def to_pf_center(driver):
    # 'center' refers to the main page of plus friend center
    driver.get(get_locators()['pf_center_url'])
    return driver

def to_pf_home(driver):
    # 'home' refers to the home page of plus friend specified in setting.json
    driver.get(get_settings()['pf_home_url'])
    return driver
