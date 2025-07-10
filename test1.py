from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://dev.tixia.com/id/checkout/order-detail?type=hotel")
driver.maximize_window()

# Tunggu elemen muncul (Explicit Wait)
wait = WebDriverWait(driver, 10)

# Fungsi untuk mengisi field dengan menunggu elemen siap
def fill_field(xpath, value):
    field = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    field.clear()
    field.send_keys(value)

# **Mulai Mengisi Data**
try:
    # Pilih Title (Mr/Mrs) - Contoh memilih "Mr"
    title_xpath = "//label[contains(text(), 'Mr')]/input"
    wait.until(EC.element_to_be_clickable((By.XPATH, title_xpath))).click()

    # Isi Nama
    fill_field("//input[contains(@id, 'react-aria')]", "John Doe")

    # Isi Email
    fill_field("//input[@type='email']", "johndoe@example.com")

    # Isi Nomor Telepon
    fill_field("//input[@type='tel']", "081234567890")

    # Isi Kota
    fill_field("//input[contains(@placeholder, 'Kota')]", "Jakarta")

    # Jika ada dropdown untuk Negara, pilih Indonesia
    country_dropdown_xpath = "//select[contains(@id, 'country')]"
    country_option_xpath = "//option[contains(text(), 'Indonesia')]"

    if wait.until(EC.presence_of_element_located((By.XPATH, country_dropdown_xpath))):
        driver.find_element(By.XPATH, country_dropdown_xpath).click()
        driver.find_element(By.XPATH, country_option_xpath).click()

    # Klik tombol Lanjut atau Submit (jika ada)
    submit_xpath = "//button[contains(text(), 'Lanjut') or contains(text(), 'Submit')]"
    wait.until(EC.element_to_be_clickable((By.XPATH, submit_xpath))).click()

    print("✅ Form berhasil diisi dan dikirim!")

except Exception as e:
    print("❌ Terjadi kesalahan:", e)

# Tunggu beberapa detik sebelum menutup browser
time.sleep(5)
driver.quit()