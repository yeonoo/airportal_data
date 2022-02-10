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


# csv파일 생성
import csv
f = open('airportalData.csv', 'a', newline='')
wr = csv.writer(f)

#시작일(st_date), 종료일(end_date) 입력
st_date = date(2020, 12, 30)
end_date = date(2021, 1, 3)

tbody_xpath = '//*[@id="mySheet-table"]/tbody/tr[3]/td/div/div[1]/table/tbody'
trSum_xpath = '//*[@id="mySheet-table"]/tbody/tr[2]/td[1]/div/table/tbody/tr[4]'
tbody = driver.find_element_by_xpath(tbody_xpath)

# tr 길이 알아내기
def trLen():
    i = 2
    tr_count = 0
    while True:
        tr_xpath = tbody_xpath + '/tr[' + str(i) + ']'
        if check(tr_xpath) != 0:
            tr_count += 1
            i += 1
        else:
            print(str(tr_count) + '개의 데이터')
            tr_count += 2
            break
    return tr_count

def dataSum():
    dataSum_xpath = '//*[@id="mySheet-table"]/tbody/tr[2]/td[1]/div/table/tbody/tr[4]'
    dataSum_tr = driver.find_element_by_xpath(dataSum_xpath)
    dataSum_list = [date, '', '']
    # 데이터 추가
    for t in range(5, 15, 1):
        sumTd_xpath = dataSum_xpath + '/td[' + str(t) + ']'
        sumTd = driver.find_element_by_xpath(sumTd_xpath)
        dataSum = sumTd.text
        dataSum_list.append(dataSum)
    wr.writerow(dataSum_list)
    print('합계 저장 완료')

# 반복
# 날짜검색-합계행저장-데이터행갯수검색-데이터행저장 순으로 반복하는 구조
for single_date in dateRange(st_date, end_date):
    date = single_date.strftime("%Y%m%d")
    dateSet('current_dt_from', date)
    dateSet('current_dt_to', date)
    print(date + ' 검색합니다.')
    searchData = '//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]'
    driver.find_element_by_xpath(searchData).click()

    # 합계 행 저장
    dataSum()

    # 데이터 행 갯수 검색 및 설정
    tr_ct = trLen()

    # 데이터행 저장
    for i in range(2, tr_ct, 1):
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
            data_list = [date, dep, arv]
            # 데이터 추가
            for m in range(5, 15, 1):
                td_xpath = tr_xpath + '/td[' + str(m) + ']'
                data_td = data_tr.find_element_by_xpath(td_xpath)
                data = data_td.text
                data_list.append(data)
            wr.writerow(data_list)
            scroll(30)
        else:
            # 노선 넣기
            data_list = [date, dep, arv]
            # 데이터 추가
            for n in range(2, 12, 1):
                td_xpath = tr_xpath + '/td[' + str(n) + ']'
                data_td = data_tr.find_element_by_xpath(td_xpath)
                data = data_td.text
                data_list.append(data)
            wr.writerow(data_list)
            scroll(30)
    print('저장 완료')

