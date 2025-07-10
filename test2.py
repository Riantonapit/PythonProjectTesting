from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)

# Fungsi untuk membuka browser dan akses Google
def open_browser():
    driver.get("http://www.google.com")
    time.sleep(5)

# Fungsi untuk mencari 'youtube' di Google
def click_search():
    input_field = driver.find_element(By.NAME, 'q')  # FIX: pakai By.NAME, bukan By class
    time.sleep(2)
    input_field.clear()
    input_field.send_keys('youtube')
    input_field.send_keys(Keys.ENTER)
    time.sleep(5)

# Jalankan fungsi
open_browser()
click_search()

# (Opsional) Tutup browser
driver.quit()

