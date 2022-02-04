# 셋팅
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=5)

# 로그인
driver.get('https://www.airportal.go.kr/common/login/login01.jsp')
login_x_path = '/html/body/form/table[3]/tbody/tr[2]/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input'
driver.find_element_by_name('df_userid').send_keys('yeonoo')
driver.find_element_by_name('df_passwd').send_keys('lyw8485!')
driver.find_element_by_xpath(login_x_path).click()

# 실시간 통계 페이지 접속
url2 = 'https://www.airportal.go.kr/knowledge/statsnew/realtime/airlineRoute.jsp#'
driver.get(url2)

# 노선 설정
from selenium.webdriver.support.select import Select
selectRoute = Select(driver.find_element_by_name("seah_ad"))
selectRoute.select_by_visible_text("제주")
selectRoute.select_by_value("RKPC")

# 날짜 지정
from selenium.webdriver.common.keys import Keys
driver.find_element_by_name('current_dt_from').clear()
driver.find_element_by_name('current_dt_from').send_keys("20220201")
driver.find_element_by_name('current_dt_from').send_keys(Keys.ENTER)
driver.find_element_by_name('current_dt_from').send_keys(Keys.BACKSPACE)
driver.find_element_by_name('current_dt_from').send_keys("1")
driver.find_element_by_name('current_dt_from').send_keys(Keys.ENTER)
driver.find_element_by_name('current_dt_to').clear()
driver.find_element_by_name('current_dt_to').send_keys("20220201")
driver.find_element_by_name('current_dt_to').send_keys(Keys.ENTER)
driver.find_element_by_name('current_dt_to').send_keys(Keys.BACKSPACE)
driver.find_element_by_name('current_dt_to').send_keys("1")
driver.find_element_by_name('current_dt_to').send_keys(Keys.ENTER)
searchData = '//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]'
driver.find_element_by_xpath(searchData).click()

# 데이터

