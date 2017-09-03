# lion(라이언)
###1. Outline, Requirement
* * *
##### English
* `lion` is automated messaging module for kakao plus friend admin. 
* You SHOULD modify `setting.json` to use this module.
  * `"admin_info"`: set admin email and password
  * `"pf_center_url"`: set url for plus friend center
  * `"chrome_driver_path"`, `"phantom_driver_path"`: set path for drivers for `selenium`.
    * required to have proper driver file(binary or exe ...) 
  * for more information about `selenium`, please check [here](http://www.seleniumhq.org/).

##### 한글
* `lion`은 카카오 플러스 친구 관리자를 위한 메세징 자동화 모듈입니다.
* 모듈을 사용하기 위해서는 `setting.json` 파일을 반드시 수정해야합니다.
  * `"admin_info"`: 관리자의 이메일과 비밀번호를 설정합니다.
  * `"pf_center_url"`: 플러스 친구 센터의 url을 설정합니다.
  * `"chrome_driver_path"`, `"phantom_driver_path"`: `selenium`에서 사용할 드라이버의 경로를 설정합니다.
    * 사용할 드라이버 파일(binary 또는 exe)이 존재해야 합니다.
  * `selenium`에 대해서는 [여기](http://www.seleniumhq.org/)를 참조해주세요.
    
  
###2. Usage
* * *
```python
import lion
lion.message.send_basic_text_message('phantom', 'msg_content', 'https://github.com/goofcode')
```

###3. API
* `lion.message.send_basic_text_message(content, link=None, share=False, mode='phantom')`
    * **send basic text type message to all friends**
    * `mode`: 'chrome' or 'phantom'(headless)
    * `content`: message content to be sent
    * `link`: link to be sent w/ message if none, only content will be send
    * `share`: whether enable 'share to friend'

*