from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
    browser.get('https://signin.aws.amazon.com/federation?Action=login&SigninToken=p1v0QaP6ggRv1ydCQMnqSkh2bOEWtf-f9CwdpuPUxuf4JtmgVehAgXiQHUVYJAM53pnJj9JlgVVaBPMndQVZpbIB3v66qftuhWw5VVuWTO10kfL_Ykuc9YQ9syIXkhVBnswkyr-2hgeyAUECkUB1a3hMMaXehwAWWD0uCBsVa71ohiFgqwx-2sPMMZhtyClcAi5bqOZjA3dw0lWNqi-MMKOB4nE12n2qqL6T53OgnKE3NuH2_yn9rUeXWQ4OeWbfho3inY_NL25sPCRAPZG3Y2vHtlPHoU81yyoMpETZLWMxTSsOd5QD1VgUScI7Z8xlams8wHW3C6EH7cWm6Xh2s9pKVXgqIFicNH7QxFwB9x35e0oaaYn_PCEaOvgPRJhfgnfV8alE3_-C08x49KPUx5MO1MbDEexYJ4VCWsxhZQSK2OKlCUkqft7NORi1A0Xnye6NDzdsurC07sMEQv15fmqCcP0EHJJuEjQG0LfCbsVtG8CWA76M1zr0jOAD0HNPVcWkWEXcjarSQCeubWGgcs_KVKApd_TZNTWGQA1FWH_cEiAh_2lEYSKWpzegqPeVZu-KFBrpYyf3OzmWdk4BduPcm05DEY85fLzYd7hs5EuziIaXEy-Ssz0ER8Heumcgdg_RTPzBosAlWAUN1zrN3ymfFfKgmKN7O_nalGqYxn13OpDh2DRezPLMZyLsydIOx88MIPGkEh_6vqFMjgeYH8q3niuOr0gzXw1QIqCT-Gg04FnGE1qPQoSByk8Fzo_gH6Xhe8E0re286wlSoo7R_hLpmHMv-z8FDbGTc0F8yLhvlsvP6iL5Qq_Jk1-oMRWMrqqaBo2l5urEQpvFaago41HmDRg-TbaWUqPY0NfbqbVfaQ-CdQ7ClWFXmd9JKarK5HCIn_dz-5wAz-m_wcE2ql14G-GKSwN_R7eJOSf4XLlOMsqzgHhjrmWwAlh1ggjjYFigeCiLcBhUDyCWR1AJ6cqcB88hODnrwe0nEnDPn8oO2N85hW4ATQxr7zua99ok4Zy_fWu72A4IDBLOSSRj4Eltt1QIhBVmu4KcQOlK7-_afLC-RpsLeFaX92DzL3Pn_2nG1IPOxldrBjse5zH6dcdgAesvfK3d8YazciWX4tGUr0uuRG3S1u6D1RI152w6cMpswgJRGBy7pyNHokt4cW8UFr9W_aixX3E3fNux93nWHNFMbrh4LZ7t09G9uYaFObEsAQvexcMzvMKDDKjk1nXl5Xlw1GtqwDWLYBIr7_RxRJw2nvKntrOp6v2B19E9IappnQc2GrJ4NIfM9rKl8OUq4nnAulUtfFi--_3NBt8UZjfPHpK1DPFzGTsGm513jEECl5sPPouWYs6bhNpqoDxm3_fePe8r1Y9oNhpEE7rqN39MHT1EfNDCN8xp4_xUBcsubDO8YUQuBl1LzcRIgpw0SyEbhfbpMQvneYs&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome')
    title = browser.title

    return title


print(handler('test','test'))