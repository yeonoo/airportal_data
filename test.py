# [참조]
from selenium import webdriver
driver = webdriver.Chrome()
# driver.implicitly_wait(time_to_wait=5)

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

# [수집 데이터 속성]
# 1. 실시간 통계 페이지 접속
url_realtime = 'https://www.airportal.go.kr/knowledge/statsnew/realtime/airlineRoute.jsp#'
driver.get(url_realtime)

# 2. 제주 노선 설정
from selenium.webdriver.support.select import Select
selectRoute = Select(driver.find_element_by_name('seah_ad'))
selectRoute.select_by_visible_text('제주')

# [데이터 출력]
# 1. 기간 설정
from datetime import date, timedelta
import time

#기간 설정 함수
def dateRange(st_date, end_date):
   for n in range(int((end_date - st_date).days)):
       yield st_date + timedelta(n)

#날짜 검색 함수
def dateSet(className, d):
    from selenium.webdriver.common.keys import Keys
    driver.find_element_by_name(className).clear()
    driver.find_element_by_name(className).send_keys(str(d))
    driver.find_element_by_name(className).send_keys(Keys.ENTER)
    driver.find_element_by_name(className).send_keys(Keys.CONTROL + 'A')
    driver.find_element_by_name(className).send_keys(str(d))
    driver.find_element_by_name(className).send_keys(Keys.ENTER)

""" 데이터 출력 전까지 주석 처리할 것
#시작일(st_date), 종료일(end_date) 입력
st_date = date(2021, 2, 1)
end_date = date(2021, 2, 5) #일자+1로 입력해야 함. 예: 2021년 2월 4일까지의 데이터가 필요하다면 2021, 2, 5로 입력할 것

# 반복
for single_date in dateRange(st_date, end_date):
    d = single_date.strftime("%Y%m%d")
    dateSet('current_dt_from', d)
    dateSet('current_dt_to', d)
    searchData = '//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]'
    driver.find_element_by_xpath(searchData).click()
"""

# 임시 날짜 설정 - 데이터 출력 완료시 이 부분 삭제하고 윗부분 살릴 것
date = '20210213'
dateSet('current_dt_from', date)
dateSet('current_dt_to', date)
searchData = '//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]'
driver.find_element_by_xpath(searchData).click()

# 데이터 추출
table = driver.find_element_by_xpath('//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody')
tr_xpath = '//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]'
data_tr = table.find_element_by_xpath(tr_xpath)
td = data_tr.find_elements_by_tag_name('td')
data_td = driver.find_element_by_xpath('//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]')

print(len(td))



