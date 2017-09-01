"""
author: Mookeun Ji, goofcode@gmail.com

# Functions defined here may raise some exceptions from driver in case of
    1. unknown change in kakao web
    2. unusual notice

  So, if there is any issue,
   going through whole messaging process manually on actual browser at least once and
   modifying this set of codes appropriately are recommended for further use
"""

import util


def send_basic_text_message(mode, content, link=None, share=True,):
    """
    send basic text type message to all friends

    :param mode: 'chrome' or 'phantom'(headless)
    :param content: message content to be sent
    :param link: link to be sent w/ message if none, only content will be send
    :param share: whether enable 'share to friend'
    """
    driver, setting, kakao = _start_and_login(mode)

    driver.get(util.url_join(setting['pf_center_url'], kakao['basic_message_url']))

    # fill inputs for new message
    driver.find_element_by_id(kakao['message_input_id']).send_keys(content)
    if link is not None:
        driver.find_element_by_xpath(kakao['add_link_radio_xpath']).click()
        driver.find_element_by_id(kakao['link_name_id']).send_keys("바로가기")
        driver.find_element_by_id(kakao['link_input_id']).clear()
        driver.find_element_by_id(kakao['link_input_id']).send_keys(link)
    if share is False:
        driver.find_element_by_xpath(kakao['no_share_radio_xpath']).click()

    driver.find_element_by_xpath(kakao['next_btn']).click()
    driver.find_element_by_xpath(kakao['submit_btn']).click()
    driver.find_element_by_xpath(kakao['confirm_btn']).click()

    import time
    time.sleep(10)


def _start_and_login(mode):

    # get new driver and data
    driver = util.get_driver(mode)
    setting = util.get_setting()
    kakao = util.get_kakao_data()

    # login to pf center
    driver.get(kakao['pf_home_url'])
    driver.find_element_by_xpath(kakao['to_login_page_btn_xpath']).click()
    driver.find_element_by_id(kakao['login_email_input_id']).send_keys(setting['admin_info']['email'])
    driver.find_element_by_id(kakao['login_pw_input_id']).send_keys(setting['admin_info']['pw'])
    driver.find_element_by_id(kakao['login_submit_btn_id']).click()

    return driver, setting, kakao

if __name__ == '__main__':
    send_basic_text_message( mode='chrome', content='Test Message', link='https://github.com/goofcode')
