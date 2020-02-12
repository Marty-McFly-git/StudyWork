from selenium import webdriver
import time

link = "https://order.nalog.ru/index.html"

browser = webdriver.Chrome()
browser.get(link)
GrabbAppleJonatan=browser.find_element_by_css_selector("body > div > div.container > div:nth-child(2) > div:nth-child(1) > div > section:nth-child(2) > ul > li:nth-child(1) > div > span > button")
GrabbAppleAdrian=browser.find_element_by_css_selector("body > div > div.container > div:nth-child(2) > div:nth-child(1) > div > section:nth-child(2) > ul > li:nth-child(2) > div.col-12.d-flex.justify-content-between.align-items-center > span > button")
GrabbAppleJulie=browser.find_element_by_css_selector("body > div > div.container > div:nth-child(2) > div:nth-child(1) > div > section:nth-child(2) > ul > li:nth-child(3) > div.col-12.d-flex.justify-content-between.align-items-center > span > button")
FreeApple=browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/section[2]/a")


FreeApple.click()
time.sleep(6)
GrabbAppleJonatan.click()
time.sleep(6)
GrabbAppleAdrian.click()
time.sleep(6)
GrabbAppleJulie.click()


def get_user_selector(n):
    return f"ul li:nth-child({n}) > div"

def get_apples_count_selector(n):
    return f"ul li:nth-child({n}) div .badge-pill"
    
def get_user_name(n):
    user_selector = get_user_selector(i)
    name = browser.find_element_by_css_selector(user_selector).text
    return name.split("\n")[0]

def get_apples_count(n):
    apples_selector = get_apples_count_selector(i)
    return browser.find_element_by_css_selector(apples_selector).text

users = {}

time.sleep(6)

for i in range(1, 4):
     user = get_user_name(i)
     print(user)
     apples = get_apples_count(i)
     print(apples)
     users[user] = apples

expected = {'Jonathan': '1', 'Adrian': '1', 'Julie': '1'}
print("Test Result: " ,users==expected)

print(users)
