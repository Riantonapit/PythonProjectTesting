from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maksimalkan jendela browser

driver = webdriver.Chrome(options=options)

def open_room_search_page():
    driver.get("https://dev.tixia.com/id/hotel/search/VT0001317?keyword=jakarta&check_in_date=2025-03-21&check_out_date=2025-03-24&guest.total_room=1&guest.total_adult=2&guest.total_child=0&search_id=4095baf5-e39d-4ac8-acf8-c6f580537e39")
    time.sleep(15)
    # print("Halaman pencarian hotel di Jakarta berhasil dibuka.")

# def select_hotel():
#     hotels = driver.find_elements(By.XPATH, "//div[contains(@class, 'hotel-list-item')]")  # Sesuaikan dengan elemen hotel
#     assert len(hotels) > 0, "Tidak ada hotel yang tersedia!"
#     hotels[0].click()
#     time.sleep(2)
#     # print("Hotel pertama berhasil dipilih.")

def book_room():
    
    # Klik tombol pesan
    choose_room_button = driver.find_element(By.CSS_SELECTOR, "#overview > div.flex.flex-row.lg\:flex-col.p-3.md\:p-6.gap-3.lg\:gap-7.justiw.lg\:justify-end.w-full.lg\:w-1\/4.border-none.lg\:border-l-2 > button")  # Sesuaikan dengan XPath tombol
    choose_room_button.click()
    time.sleep(5)
    print("Pemesanan hotel berhasil!")

    book_room_button = driver.find_element(By.CSS_SELECTOR, "#rooms > div > div.w-full.md\:w-\[75\%\].lg\:\[70\%\].px-3.md\:px-0 > div > div.flex.justify-between > div.flex.flex-col.gap-2.lg\:gap-1.px-0.pb-4.pt-2.flex-1 > div:nth-child(3) > button")
    book_room_button.click()
    time.sleep(5)
    
def close_browser():
    driver.quit()

# Jalankan test
open_room_search_page()
book_room()
close_browser()
