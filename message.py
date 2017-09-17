"""
author: Mookeun Ji, goofcode@gmail.com

Functions defined here may raise some exceptions from driver in case of

    1. setting or locator fault
    2. loss of internet connection
    3. ==unknown change in kakao web==
    4. ==unusual notice==

  So, if there is any issue,
   going through whole messaging process manually on actual browser at least once and
   modifying this set of codes appropriately are recommended for further use
"""

from .util import *

def send_basic_text_message(content, time=None, link=None, share=True, mode='phantom'):
    """
    send basic text type message to all friends

    :param content: message content to be sent
    :param [opt] time: time message to be sent(formatted as yyyymmdd hh:mm, if none, time set to be now
    :param [opt] link: link to be sent w/ message if none, only content will be send
    :param [opt] share: whether enable 'share to friend'
    :param [opt] mode: 'chrome' or 'phantom'(headless)
    """

    driver = get_driver(mode)
    settings, locators = get_settings_and_locators()

    login_pf_center(driver)
    driver.get(url_join(settings['pf_home_url'], locators['basic_message_url']))

    # fill inputs for new message
    wait_until_load(driver, 'id', locators['message_input_id']).send_keys(content)

    if link is not None:
        wait_until_load(driver, 'xpath', locators['add_link_radio_xpath']).click()
        wait_until_load(driver, 'id', locators['link_name_id']).send_keys("바로가기")
        wait_until_load(driver, 'id', locators['link_input_id']).clear()
        wait_until_load(driver, 'id', locators['link_input_id']).send_keys(link)

    if share is False:
        wait_until_load(driver, 'xpath', locators['no_share_radio_xpath']).click()

    wait_until_load(driver, 'xpath', locators['next_btn_xpath']).click()

    '''
     TODO : add time feature
    
    if time is not None:
        d_time = datetime.datetime.strptime(time, '%Y%m%d %H:%M')
        wait_until_load(driver, 'class', locators['show_calendar_class']).click()
    '''

    wait_until_load(driver, 'xpath', locators['submit_btn_xpath']).click()
    wait_until_load(driver, 'xpath', locators['confirm_btn_xpath']).click()

    driver.close()

