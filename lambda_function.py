from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handler(event, context):
    print("Starting google.com")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get('https://signin.aws.amazon.com/federation?Action=login&SigninToken=ANX43_vk6ToEUEPZrMHO5UFPSeqKyplFmw3rYQ0221H45WvG-x2UOtEjp4zS8w5gWrdEnoEN7h3xPEpmreQT6-Sd74TKgAgYnUrNlUF_ADS2qbWLCsoI1jEf3vYIhb9PaSWA5iw5TNhrtlNCUNypxOsx3tZEQsYAhP8t8hDTj5FhaYKUpQT72QDQmBwXYKeATAt1-z9lPbOcRXazr4Wg412cyWl6EmofLLiqVpEHcGtP-eEIhVcK8r1SZ7Gc6u059HyBAidky9ZtVHJwN7Eu4wvnuWADVXYtr1XhACmVTPWGyb7PSsPBcYOpTu8c3x7zX67E6DoRYiwIQHMKZzXBVVW6Ga2X6dK-3-I8eAL2VRLQWUxuckI0ymXDl6PFuzsZNDj5PIvxL4TspmvrrvNNRa2dOafUV2ropG9_S6C7BhrJl4qtNtAW0aUbGl-qwYLFnM5BeHOZOEopZba_6iy4UZ44UjrRIGbEHtgIhteTqlqfyNeW2jkFv9QNmJ6S2zBmqlSZPuA42P7fGDw-vjSI1o4PK_AlZSFfTJHrzNKXt4CLb2bkg2-YO1k2oSFBMf4N4Wpu8NymcY5FZnCl_9l-CLMFepB6EZJik5PU4ntO5IaBkdPQUSCJsISHLPulNDvdIFieH0DCbsz-UBaDV7Dar203D-F6QKBKRSTQBZyf96UK2WTgAtoIusXG8jVKdzks4B5JKjtRnk8vE8WdnNFX-T3Qh_rPwz7MZIo5dEWAP0gXdo7t3aN4IoBauwoYZqdK9PvonakAmq5477N_XjZSnzsbggLCdVypq8yldEbZTMpgplvVzS9iidWfU_ytPKSH-b1RMAUMRqz1_0IfeKaZu6Iw0xNYGVIi7F4GOLqch3dU3Aci2NjEAQ160H4tgef8p-sJN5VjLPr1-nWTIBaSV4WhfYyla3pJ2Cj_YaBoXIi2YZChnZrFJlup_oKRQteSTfLDgR-c6-7DY65tF662QBK4w9qx4fdOGcFzOgOyEayqxgA0vNbzDtRw2sT5am52ti0nnPy6Ycg2yuVWL1t8QIsTSpp4AlRBRpPf2oDVD-sIXxd7RfI_UE8B8FbYE5ITmyZZFbaz8mtHPQ_Qa2KfWx6CEXBbTsGBRLHklZD--bvmQEuaoDWgdxk1xNmr6BHB5fSdgxicS52Gs1ilXAFBA_5MlDuZ2ngJPzu0Z1t2FxqxrSxxqMVVj4iZPO5hdo795usOOcucAO65fa9vL92ECXnGzdF339Xdxkfow7eNDlnncx30DauIsRibE_PDORtMnhiHgB_JXdsUdGQYgWUNhtw2kbY_lC1zBOD0AnpGBahWx-kI4CUWGe5NxxSWnM6fmQzEyD85ZPnfqaZZ3O6ZZrozlFGzeqPZ0Q8DHdpRi9BWqRT8P_nBplWA2u4TyFt4g3cK2Lyx7nC_9t7BUCAW1X54FJYlqe0vGJzS1jM&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome')
    browser.get('https://health.aws.amazon.com/health/home#/account/event-log')
    title = browser.title
    print(title)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

    change_table = browser.find_element(By.TAG_NAME,"table")
    print(change_table.text)
    change_trs = change_table.find_element(By.TAG_NAME,"tbody").find_elements(By.TAG_NAME,"tr")
    print(change_trs)


    for change_tr in change_trs:

        change_tds = change_tr.find_elements(By.TAG_NAME,"td")
        print(change_tds)
        for td_idx, change_td in enumerate(change_tds):
            print(td_idx,change_td.text)

        print(f"\n")

    return title


print(handler('test','test'))