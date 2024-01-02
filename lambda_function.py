from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


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
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get('https://signin.aws.amazon.com/federation?Action=login&SigninToken=FhpkkrS18XfhCPJSZb-5vA_1FlN8OCCaalRXfj2d_jwO16NxVgr7dRuiNmCL8okwGrCj06zk9LMW8KtpvYMP1rmLIHNO3FdaihvTlDv_KQoRMuep3s0a4Ze_zK-MAb_xH96yQXFsOXAiaMmRAzq_hwqj35HOgHkrO75gZmNZ0YkUp-1xdLiliU2NJrOz5WzP7Zm6JTX7juToAnMJCmYsJ0uZ212n9r4Deqlj74_Ilo_TjBPgRnWlnbGcOYqPlVxV0KYPGxyg-cIpiN0Yr_ZFStmg4szYVOVoS_IiZGtZWXNn7OKAshDyqopwUnjButrLd51JsRr91RzwKwEkC-_YugMWqkfXjfLXLSlFKimZlNaaix4386TSrP1zyZIStDTuOiPLqWkCHFIGHzOxq924JK1fmB_5V60n5MWjTcbRzIaoC_u7htJIxw-uzq4Mjg41KYw07Ec1Vs_Fef8DATSKYuyfJPx2HaZwcgMUKFfP7liUruxs9ltfkFF9cXozP3oPtcOKa7nkGDe_9iQVVQy556OrKFDRegD_W7hA0cjBLUyxslT1GOIZzpUPqDtMhE7gQJ4Prq-F4bW1HtTbSFrRItOfDn7jHHrezL8_Ng4mW3d5nunHO4S57F53BEOlKgZhiKTbc8cDe_WW03IGm7jKWEOSlfQ11fItUiqCD1pCPAvxc3U17jV04Y7fklS8Q6NWwRh1k_aLGZxX3zxq3THgugck1NiUgsjbW0RqVQ7_Ywc274Ljge3GqfnlJYMLPcCeU5xxPgnElqEYGTfaNgcZ_-IrNkAsxykTGwGHRd7CauhzHHrvZw-LzHM0GTR_IeS82QY74N1AvPhBZeZlvamTgrTQKpB4QJ6L8BaEBmWr9b4ZJROxDM7eUfu1zsL5u2eiYr1M-sP_LtaoDfYcYXqDjsqafpj3CK_kLlIt34jYP7zlaaqmKVzzMShTSDH2Jat6YSzzunCyb3q1G2TLWG3622vzHRhv_l-JgFI_NCe06RhuMjBD2eYPi62AeHesFANI5vWo4YY6wjf7gEDbtB-op4HOofvROma21j36sRySJmFzaw3-GjPN6c8sksPPlwJ5ezdgOjfMbbryrLuziVzfEvBY4Hauhti398tIxWnGuDOBNxXEURn7p9OuJd06MY7pY9BhGeKQ-H1tE1rj1Gm3GLKgYRRf3GqHP9--Wgrabuh6_cj9U85482U8j2nKtgiHD8e15J6bcxTs_yiHaEJmukiqgu_GodRxa6xWg-gGggD-rhNbyIQC_KK49DxAXXfSU5OZ0gNzMdRnhGvkCRWISxMEw4AdLxk5FoZRKkNizadD32yRiU2HZGk-i5TuMD-h4LUujnMtTMQ2GVM6o8cK-PPlW2g_vrriHSrmBBJ7qmF1SQlzh1xgUpWQ0na8PE12BMRL-Eu7XpbhOkRcU4q0rdizGntsuEA9Kc8jbWfqPJdWZyEUWSZVWqY&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome')

    time.sleep(1)

    browser.get('https://health.aws.amazon.com/health/home#/account/event-log')

    time.sleep(1)

    title = browser.title
    print(title)

    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

    change_table = browser.find_element(By.TAG_NAME,"table")
    change_trs = change_table.find_element(By.TAG_NAME,"tbody").find_elements(By.TAG_NAME,"tr")
    print(change_trs)
    for change_tr in change_trs:
        change_tds = change_tr.find_elements(By.TAG_NAME,"td")
        eventlink = change_tds[1].find_element(By.TAG_NAME,"a")
        browser.execute_script("arguments[0].click()",eventlink)

        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By., 'table')))

        print(f"\n")


handler('test','test')