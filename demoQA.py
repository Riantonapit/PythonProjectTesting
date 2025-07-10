from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
user_data_dir = tempfile.mkdtemp()
options.add_argument(f' --user-data-dir={user_data_diri}')

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

def open_website():
    driver.get('https://demoqa.com/text-box')
    time.sleep(5)

def fill_input():
    input_username= driver.find_element(By.ID, 'userName')
    input_username.clear()
    input_username.send_keys('Rianto Napitupulu')
    time.sleep(2)

    input_email= driver.find_element(By.ID, 'userEmail')
    input_email.clear()
    input_email.send_keys('rian@gmail.com')
    time.sleep(2)

    input_current_address=driver.find_element(By.ID, 'currentAddress')
    input_current_address.clear()
    input_current_address.send_keys('jalan kenangan')
    time.sleep(2)

    input_permanent_address=driver.find_element(By.ID, 'permanentAddress')
    input_permanent_address.clear()
    input_permanent_address.send_keys('jalan jalan ke kota baru')
    time.sleep(2)

def click_submit():
    click_submit_button= driver.find_element(By.ID, 'submit')
    click_submit_button.click()
    time.sleep(2)

def close_browser():
    driver.quit


open_website()
fill_input()
click_submit()
close_browser()
