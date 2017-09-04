"""
author: Mookeun Ji, goofcode@gmail.com

# Functions defined here may raise some exceptions from driver in case of

    1. setting or locator fault
    2. loss of internet connection
    3. ==unknown change in kakao web==
    4. ==unusual notice==

  So, if there is any issue,
   going through whole messaging process manually on actual browser at least once and
   modifying this set of codes appropriately are recommended for further use
"""

from util import *

def send_basic_text_message(content, link=None, share=True, mode='phantom'):
    """
    send basic text type message to all friends

    :param content: message content to be sent
    :param link: link to be sent w/ message if none, only content will be send
    :param share: whether enable 'share to friend'
    :param mode: 'chrome' or 'phantom'(headless)

    """

    driver = get_driver(mode)
    settings, locators = get_settings_and_locators()

    login_pf_center(driver)
    driver.get(url_join(settings['pf_home_url'], locators['basic_message_url']))

    # fill inputs for new message
    wait_until_id_load(driver, locators['message_input_id']).send_keys(content)

    if link is not None:
        wait_until_xpath_load(driver, locators['add_link_radio_xpath']).click()
        wait_until_id_load(driver, locators['link_name_id']).send_keys("바로가기")
        wait_until_id_load(driver, locators['link_input_id']).clear()
        wait_until_id_load(driver, locators['link_input_id']).send_keys(link)

    if share is False:
        wait_until_xpath_load(driver, locators['no_share_radio_xpath']).click()

    wait_until_xpath_load(driver, locators['next_btn_xpath']).click()
    wait_until_xpath_load(driver, locators['submit_btn_xpath']).click()
    wait_until_xpath_load(driver, locators['confirm_btn_xpath']).click()

    driver.close()
