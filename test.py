# 셋팅
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=5)

# 로그인
driver.implicitly_wait(3)
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
select = Select(driver.find_element_by_name("seah_ad"))
select.select_by_visible_text("제주")
select.select_by_value("RKPC")

# 날짜 지정
# 날짜 지정
from selenium.webdriver.common.by import By
# driver.findElement(By.name("current_dt_from")).sendKeys("value", "20220201")
# driver.findElement(By.name("current_dt_to")).sendKeys("value", "20220201")
driver.find_element_by_id(("dateStart")).send_keys("value", "20220201")
driver.find_element(By.id("dateEnd")).send_keys("value", "20220201")

# 데이터

