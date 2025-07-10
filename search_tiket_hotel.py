from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maksimalkan jendela browser

driver = webdriver.Chrome(options=options)

# def wait_for_element(xpath):
#     return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

def open_page():
    driver.get("https://dev.tixia.com/id")
    time.sleep(2)

    hotel_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[1]/div[2]/div/div/div[2]/div[2]")
    hotel_button.click()
    time.sleep(5)


# def open_hotel_page():
#     driver.get("https://dev.tixia.com/id/hotel")  # Langsung ke halaman hotel
#     time.sleep(2)

def search_hotel():
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[1]/div[2]/div/div/div[1]/button")
    button.click()
    time.sleep(1)

    input_field = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/section/div[2]/div[1]/input")
    input_field.clear()
    input_field.send_keys("bali")
    time.sleep(5)
    # print(f"Teks '{text}' berhasil dimasukkan ke dalam input dengan XPath '{xpath}'.")

    select_input_field = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/section/div[2]/div[2]/div[1]/div[1]/div")
    select_input_field.click()
  
    date_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div > main > div > div.relative.w-full.h-\[630px\].flex.flex-col > div.z-30.w-full.flex.flex-col.my-auto.max-w-screen-2xl.mx-auto > div > div > div.w-full.flex.flex-col.md\:flex-row.flex-1.justify-between.gap-y-5.gap-x-10 > div > button")
    date_button.click()
    time.sleep(2)

    checkin_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table")
    checkin_input.click()

# Pilih tanggal check-in (misalnya: 20 Maret 2025)
    checkin_date = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[5]/button")
    checkin_date.click()

# Pilih tanggal check-out (misalnya: 25 Maret 2025)
    checkout_date = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table/tbody/tr[5]/td[1]/button")
    checkout_date.click()
    time.sleep(1)

    # guest_and_room_picker = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div > main > div > div.relative.w-full.h-\[630px\].flex.flex-col > div.z-30.w-full.flex.flex-col.my-auto.max-w-screen-2xl.mx-auto > div > div > div.flex.flex-col.xl\:flex-row.w-full.xl\:w-1\/3.items-center.gap-4.gap-y-5 > div.flex.flex-col.flex-1.w-full.xl\:w-fit > button")
    # guest_and_room_picker.click()
    # time.sleep(1)



    # checkin_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[5]/button")
    # checkin_input.click()
    # time.sleep(1)
    # checkout_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[7]/button")
    # checkout_input.click()
    
    # Pilih tanggal check-in dan check-out
    # input_text_by_xpath("//input[@name='checkin']", "15/03/2025")
    # input_text_by_xpath("//input[@name='checkout']", "17/03/2025")
    
    # Tekan tombol cari
    search_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div > main > div > div.relative.w-full.h-\[630px\].flex.flex-col > div.z-30.w-full.flex.flex-col.my-auto.max-w-screen-2xl.mx-auto > div > div > div.flex.flex-col.xl\:flex-row.w-full.xl\:w-1\/3.items-center.gap-4.gap-y-5 > div:nth-child(2) > button")  # Sesuaikan dengan XPath tombol pencarian
    search_button.click()
    time.sleep(15)  # Tunggu hasil pencarian
    
    # Validasi hasil pencarian
    # results = driver.find_elements(By.XPATH, "//div[contains(@class, 'hotel-list-item')]")  # Sesuaikan dengan elemen yang benar
    # assert len(results) > 0, "Tidak ada hasil yang ditemukan!"

def choose_ticket_hotel():
    book_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div > section > section > section > section.flex.items-start.gap-x-10.w-full > div.flex.flex-col.pt-\[7\.3rem\].lg\:pt-0.w-full.lg\:w-4\/5 > div > div:nth-child(1) > div.flex.flex-row.md\:flex-col.w-full.md\:w-1\/4.px-3.md\:px-6.pb-5.pt-2.lg\:py-7.md\:py-5.gap-4.h-full > div.hidden.md\:flex.justify-end.items-end.min-h-10 > button")  # Sesuaikan dengan XPath tombol
    book_button.click()
    time.sleep(5)

def book_room():
    
    # WebDriverWait(driver, 5).until (
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#overview > div.flex.flex-row.lg\:flex-col.p-3.md\:p-6.gap-3.lg\:gap-7.justiw.lg\:justify-end.w-full.lg\:w-1\/4.border-none.lg\:border-l-2 > button"))
    # )
    # Klik tombol pesan
    # choose_room_button = driver.find_element(By.CSS_SELECTOR, "#overview > div.flex.flex-row.lg\:flex-col.p-3.md\:p-6.gap-3.lg\:gap-7.justiw.lg\:justify-end.w-full.lg\:w-1\/4.border-none.lg\:border-l-2 > button")  # Sesuaikan dengan XPath tombol
    # choose_room_button.click()
    # time.sleep(5)

    wait = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH,    "/html/body/div[1]/div/section/div/section/section/section/div[3]/div[1]/div[2]/button"))
    )
    
    # Klik tombol pesan
    choose_room_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/section/section/section/div[3]/div[1]/div[2]/button")  # Sesuaikan dengan XPath tombol
    choose_room_button.click()
    time.sleep(5)
    print("Pemesanan hotel berhasil!")

    book_room_button = driver.find_element(By.CSS_SELECTOR, "#rooms > div > div.w-full.md\:w-\[75\%\].lg\:\[70\%\].px-3.md\:px-0 > div > div.flex.justify-between > div.flex.flex-col.gap-2.lg\:gap-1.px-0.pb-4.pt-2.flex-1 > div:nth-child(3) > button")
    book_room_button.click()
    time.sleep(5)

def close_browser():
    driver.quit()

# Jalankan test
open_page()
search_hotel()
choose_ticket_hotel()
book_room()
close_browser()
