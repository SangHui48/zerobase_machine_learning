import pandas as pd
import time
from selenium import webdriver
from tqdm import tqdm

# 웹 브라우저가 없는 상황에서 
# 램 상에서만 셀레니움 컨트롤 시키기
options = webdriver.ChromeOptions()
options.add_argument("headless")

url = "https://finance.naver.com/marketindex/"
# driver = webdriver.Chrome("driver/chromedriver.exe")
driver = webdriver.Chrome("driver/chromedriver.exe", options=options)
driver.get(url)
driver.maximize_window()
time.sleep(3)

# 스크롤 하기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# iframe 태그 지정
iframe = driver.find_element_by_css_selector("#frame_ex1")

# irame 태그 이동
driver.switch_to_frame(iframe)
time.sleep(3)

contents = driver.find_elements_by_css_selector("body > div > table > tbody > tr")

datas = []

for content in tqdm(contents):
    title = content.find_element_by_css_selector(".tit > a").text
    sale = content.find_element_by_css_selector(".sale").text
    link = content.find_element_by_css_selector(".tit > a").get_attribute("href")
    datas.append({
        "title": title,
        "sale": sale,
        "link": link
    })
    time.sleep(3)

df = pd.DataFrame(datas)
df.to_excel("source_code/sel_naver_finance.xlsx", encoding="utf-8")

driver.quit()