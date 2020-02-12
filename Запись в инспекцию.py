from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

link = "https://order.nalog.ru/index.html"

browser = webdriver.Chrome()
browser.get(link)

Agree=browser.find_element_by_css_selector("#content > div > div:nth-child(2) > div > p:nth-child(3) > a.button.button-rounded.button-reveal.button-large.tright > span")

Agree.click()

Radio=browser.find_element_by_css_selector("#ctl00_face_RB1 > tbody > tr > td.dxichTextCellSys > label")
Next=browser.find_element_by_css_selector("#ctl00_btNext")

Radio.click()
browser.find_element_by_id('ctl00_LastName_I').send_keys('Филиппова')
browser.find_element_by_id('ctl00_FirstName_I').send_keys('Елизавета')
browser.find_element_by_id('ctl00_email_I').send_keys('ee.filippova@fcod.nalog.ru')
Next.click()

browser.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div/div/div[2]/div/table[1]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td[2]/input').send_keys('40')

