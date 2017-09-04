import re
import time

import util


def get_friend_number(mode='phantom'):
    """
    :param mode: 'chrome' or 'phantom'(headless)
    :return: (int) number of friend of plus friend
    """
    driver = util.get_driver(mode)
    util.login_pf_center(driver)
    util.to_pf_home(driver)

    friend_element = util.wait_until_xpath_load(driver, util.get_locators()['friend_number_xpath'])
    # friend number is loaded dynamically
    time.sleep(2)
    friend_number = int(re.findall(r'\d+', friend_element.text)[0])
    driver.close()
    return friend_number

def get_left_free_message_number(mode='phantom'):
    """
    :param mode: 'chrome' or 'phantom'(headless)
    :return: (int) number of left free message
    """
    driver = util.get_driver(mode)
    util.login_pf_center(driver)
    util.to_pf_home(driver)

    free_message_element = util.wait_until_xpath_load(driver, util.get_locators()['free_message_xpath'])
    # left_free_message_number is loaded dynamically
    time.sleep(2)
    free_message = int(free_message_element.text.replace(',', ''))
    driver.close()
    return free_message

