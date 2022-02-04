# 셋팅
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=5)

# [로그인]
# 1. 로그인 페이지 접속
url_login = 'https://www.airportal.go.kr/common/login/login01.jsp'
driver.get(url_login)
# 2. 로그인 정보 입력
driver.find_element_by_name('df_userid').send_keys('yeonoo')
driver.find_element_by_name('df_passwd').send_keys('lyw8485!')
# 3. 로그인 버튼 클릭
login_button = '/html/body/form/table[3]/tbody/tr[2]/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input'
driver.find_element_by_xpath(login_button).click()

# 실시간 통계 페이지 접속
url_realtime = 'https://www.airportal.go.kr/knowledge/statsnew/realtime/airlineRoute.jsp#'
driver.get(url_realtime)

# 제주 노선 설정
from selenium.webdriver.support.select import Select
selectRoute = Select(driver.find_element_by_name('seah_ad'))
selectRoute.select_by_visible_text('제주')

# 날짜 지정
from selenium.webdriver.common.keys import Keys
# 1. 출발일 날짜 입력
driver.find_element_by_name('current_dt_from').clear()
driver.find_element_by_name('current_dt_from').send_keys('20220201')
driver.find_element_by_name('current_dt_from').send_keys(Keys.ENTER)
driver.find_element_by_name('current_dt_from').send_keys(Keys.CONTROL + 'A')
driver.find_element_by_name('current_dt_from').send_keys('20220201')
driver.find_element_by_name('current_dt_from').send_keys(Keys.ENTER)
# 2. 도착일 날짜 입력
driver.find_element_by_name('current_dt_to').clear()
driver.find_element_by_name('current_dt_to').send_keys('20220201')
driver.find_element_by_name('current_dt_to').send_keys(Keys.ENTER)
driver.find_element_by_name('current_dt_to').send_keys(Keys.CONTROL + 'A')
driver.find_element_by_name('current_dt_to').send_keys('20220201')
driver.find_element_by_name('current_dt_to').send_keys(Keys.ENTER)
searchData = '//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]'
driver.find_element_by_xpath(searchData).click()

# 데이터 추출
data_tbody = driver.find_element_by_xpath('//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody')
data_tr = data_tbody.find_elements_by_tag_name('tr')
for td in data_tr:
    data_row = td.text
    data_row_list = data_row.split('\n')
    print(data_row_list)

import _csv
def crawl():
    column_list = ["출발지", "도착지", "항공사", "운항출발", "운항도착", "운항계", "여객출발", "여객도착", "여객계", "화물출발", "화물도착", "화물계"]
    w =
"""
1. xpath로 티바디 접근
2. xpath로 티알 접근
3. 2로 td 접근
4. td를 리스트 형태로 저장
"""
