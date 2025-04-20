from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

dr = webdriver.Chrome()
log_url = "https://www.flipkart.com/"
dr.maximize_window()
dr.get(log_url)
auto_click_on = dr.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
uset_id_login = "---------------"
filling_user_input= dr.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']").send_keys(uset_id_login)
req_otp = dr.find_element(By.XPATH,"//button[normalize-space()='Request OTP']").click()
# otp manually
time.sleep(15)

# 1. product search for automation

search_box = WebDriverWait(dr,10).until(
    EC.presence_of_element_located(By.CSS_SELECTOR,"input[placeholder='Search for Products, Brands and More']")
)
search_box.send_keys("iphone 16 pro")
search_box.submit()
time.sleep(3)