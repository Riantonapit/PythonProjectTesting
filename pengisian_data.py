from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maksimalkan jendela browser
service = Service(executable_path="")
driver = webdriver.Chrome(options=options)

def open_checkout_page():
    driver.get("https://dev.tixia.com/id/checkout/order-detail?type=hotel")
    time.sleep(3)

def fill_data():

    # wait = WebDriverWait(driver, 10)
    radio_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[1]/div/div/label[1]/input")
    radio_button.click()
    time.sleep(3)
    
    field_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[2]/div/div/div/div/input")
    field_name.clear()
    field_name.send_keys("John")
    time.sleep(3)

    phone_number = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[3]/div[1]/div/input")
    phone_number.clear()
    phone_number.send_keys("081232132132")
    time.sleep(3)

    field_email = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[3]/div[2]/div/div/div/div/input")
    field_email.clear()
    field_email.send_keys("ryanleonel8@gmail.com")
    time.sleep(3)

    order_for = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[4]/div/div[2]/div/div/label[1]/input")
    order_for.click()
    time.sleep(3)

    tamu_kamar = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[4]/div/div[3]/div/div/h2/button/div/span")
    tamu_kamar.click()
    time.sleep(3)

    WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[4]/div/div[3]/div/div/section/div/div[2]/div[1]/div/div/label[1]/input"))
    )

    tamu_title = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/section[2]/section[1]/div[1]/div[4]/div/div[3]/div/div/section/div/div[2]/div[1]/div/div/label[1]/input")
    tamu_title.click()
    time.sleep(3)



def close_browser():
    driver.quit()

# Jalankan test
open_checkout_page()
fill_data()
close_browser()