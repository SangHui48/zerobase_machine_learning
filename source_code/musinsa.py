
import pandas as pd
import time
import requests
from selenium import webdriver
from tqdm import tqdm_notebook

# explicitly wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("headless")

url = "https://store.musinsa.com/app/"
driver = webdriver.Chrome("../driver/chromedriver.exe", options=options)
# 웹 페이지 전체가 로딩 될 때까지 10초간 대기하고, 10초 안에 로딩이 완료되면 다음 코드를 실행
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

# 로그인 버튼 클릭
WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "#default_top > div.header-member > button"))).\
    click()

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > input:nth-child(2)"))).\
        send_keys("vodlrm123")

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > input:nth-child(3)"))).\
        send_keys("tkdgml3#")

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > button"))).\
        click()

best_link = driver.find_element_by_css_selector("#ui-id-2 > ul:nth-child(1) > li:nth-child(1) > a").get_attribute("href")

driver.execute_script(f'window.open("{best_link}")')

# 탭 이동 하기
driver.switch_to_window(driver.window_handles[1])

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn_exclusive"))).\
        click()

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn_sale"))).\
        click()

# 금액 단위 설정하기

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "#minPrice"))).\
        send_keys("10000")

WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "#maxPrice"))).\
        send_keys("100000")

# 검색 버튼 클릭하기
WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn_price_search"))).\
        click()

# 부모 태그
outers = driver.find_elements_by_css_selector("#searchList > li")

datas = []

for outer in tqdm_notebook(outers[:3]):
    title = outer.find_element_by_css_selector("p.list_info > a").get_attribute("title")
    price = outer.find_element_by_css_selector("p.price").text.split(" ")[1][:-1]
    sale = outer.find_element_by_css_selector(".icon_new").text.split(" ")[1][:-1]
    link = outer.find_element_by_css_selector(".list_img > a").get_attribute("href")
    img = outer.find_element_by_css_selector(".list_img > a > img").get_attribute("data-original")
    datas.append({
        "title": title,
        "price": price,
        "sale": sale,
        "link": link,
        "img": img
    })

driver.quit()
df = pd.DataFrame(datas)
df.to_excel("./musinsa/musinsa.xlsx",encoding="utf-8")

# 이미지 다운로드

for idx, rows in tqdm_notebook(df.iterrows()):
    thumb_link = rows["img"]
    response = requests.get(thumb_link)
    name = f'{idx}_{rows["title"]}'
    with open("musinsa/{}.png".format(name), "wb") as f:
        f.write(response.content)
