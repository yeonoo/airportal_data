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

# 기간 설정 함수
def dateRange(st_date, end_date):
    for n in range(int((end_date - st_date).days)):
        yield st_date + timedelta(n)

# 날짜 검색 함수
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
# 행이 존재하는지 확인하는 함수
from selenium.common.exceptions import NoSuchElementException
def check(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def scroll(i):
    scroll_tbody = driver.find_element_by_xpath('//*[@id="mySheet-table"]/tbody')
    itemlist = scroll_tbody.find_element_by_xpath('//*[@id="mySheet-table"]/tbody/tr[2]/td[2]/div/div')
    driver.execute_script("arguments[0].scrollBy(0,"+str(i)+")", itemlist)


tbody_xpath = '//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody'
trSum_xpath = '//*[@id="mySheet-table"]/tbody/tr[2]/td[1]/div/table/tbody/tr[4]'
tbody = driver.find_element_by_xpath(tbody_xpath)

# tr 길이 알아내기
i = 2
tr_count = 0
while True:
    tr_xpath = tbody_xpath + '/tr[' + str(i) + ']'
    if check(tr_xpath) != 0:
        tr_count += 1
        i += 1
    else:
        print(tr_count)
        tr_count += 2
        break

for i in range(2, tr_count, 1):
    tr_xpath = tbody_xpath + '/tr[' + str(i) + ']'
    data_tr = driver.find_element_by_xpath(tr_xpath)
    td_14_xpath = tr_xpath + '/td[14]'

    # 데이터 추출
    if check(td_14_xpath) != 0:
        # 노선 넣기
        tdDep_xpath = tr_xpath + '/td[3]'
        td_dep = data_tr.find_element_by_xpath(tdDep_xpath)
        dep = td_dep.text
        tdArv_xpath = tr_xpath + '/td[4]'
        td_arv = data_tr.find_element_by_xpath(tdArv_xpath)
        arv = td_arv.text
        data_list = [dep, arv]
        for m in range(5, 15, 1):
            td_xpath = tr_xpath + '/td[' + str(m) + ']'
            data_td = data_tr.find_element_by_xpath(td_xpath)
            data = data_td.text
            data_list.append(data)
        print(data_list)
        scroll(30)

    else:
        # 노선 넣기
        data_list = [dep, arv]
        for n in range(2, 12, 1):
            # 데이터 추가
            td_xpath = tr_xpath + '/td[' + str(n) + ']'
            data_td = data_tr.find_element_by_xpath(td_xpath)
            data = data_td.text
            data_list.append(data)
        print(data_list)
        scroll(30)