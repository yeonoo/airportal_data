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

## 데이터 추출하기
import pandas as pd
import numpy as np
from selenium.common.exceptions import NoSuchElementException

## 필요 함수
#행이 존재하는지 확인하는 함수
def check(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# 합계 리스트 생성하는 함수(1번 TD)
def dataSum():
    total_tr_xpath = '//*[@id="mySheet-table"]/tbody/tr[2]/td[1]/div/table/tbody/tr[4]'
    total_tr = data_tbody.find_element_by_xpath(total_tr_xpath)
    dataSum_list = ['', '']
    for i in range(5, 15, 1):
        td_xpath = total_tr_xpath + '/td[' + str(i) + ']'
        data_td = total_tr.find_element_by_xpath(td_xpath)
        data = data_td.text
        dataSum_list.append(data)
    print(dataSum_list)

# 데이터 리스트를 생성하는 함수
def dataList():
    tr_num = 2
    tr_xpath = '//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[' + str(tr_num) + ']'
    while True:
        data_tr = data_tbody.find_element_by_xpath(tr_xpath)
        st_xpath = tr_xpath + '/td[3]'  # 출발지 노선명 xpath
        ar_xpath = tr_xpath + '/td[4]'  # 도착지 노선명 xpath
        st_td = data_tr.find_element_by_xpath(st_xpath)  # 출발지 노선명 찾기
        ar_td = data_tr.find_element_by_xpath(ar_xpath)  # 도착지 노선명 찾기
        st = st_td.text  # 출발지 노선명 텍스트
        ar = ar_td.text  # 도착지 노선명 텍스트
        if check(tr_xpath):
            td_14_xpath = tr_xpath + ']/td[14]'
            data_list = [st, ar]  # 앞머리에 저장
            if check(td_14_xpath): #14번 TD가 존재하는가?
                for m in range(2, 12, 1): #5TD부터 14TD까지 데이터 추출
                    td_xpath = tr_xpath + '/td[' + str(m) + ']'
                    data_td = data_tr.find_element_by_xpath(td_xpath)
                    data = data_td.text
                    data_list.append(data)
                    print(data_list)
            else: #14번 TD가 있는 경우(출발/도착지 병합처리)
                for n in range(5, 15, 1): #2TD부터 11TD까지 데이터 추출
                    td_xpath = tr_xpath + '/td[' + str(n) + ']'
                    data_td = data_tr.find_element_by_xpath(td_xpath)
                    data = data_td.text
                    data_list.append(data)
                    print(data_list)
        else:
            tr_num += 1

# 기본 지정
data_list = []
data_tbody = driver.find_element_by_xpath('//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody')


dataSum()
dataList()
print(data_list)









# while TR이 없을 때까지
#     dataSum()
#     td =+1




# # TD+1
#
# # 14번 TD가 존재하는가?
# 출발 = TD3
# 도착 = TD4
# td5~14 리스트 삽입
#
# #14번 TD가 존재하지 않음
# 출발=TD3
# 도착 = TD4
# TD2~11
# 리스트 출력



