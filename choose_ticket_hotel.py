from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maksimalkan jendela browser

driver = webdriver.Chrome(options=options)

def open_hotel_search_page():
    driver.get("https://dev.tixia.com/id/hotel/search?keyword=jakarta&check_in_date=2025-03-21&check_out_date=2025-03-24&guest.total_room=1&guest.total_adult=2&guest.total_child=0")
    time.sleep(15)
    # print("Halaman pencarian hotel di Jakarta berhasil dibuka.")

# def select_hotel():
#     hotels = driver.find_elements(By.XPATH, "//div[contains(@class, 'hotel-list-item')]")  # Sesuaikan dengan elemen hotel
#     assert len(hotels) > 0, "Tidak ada hotel yang tersedia!"
#     hotels[0].click()
#     time.sleep(2)
#     # print("Hotel pertama berhasil dipilih.")

def book_hotel():
    
    # Klik tombol pesan
    book_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div > section > section > section > section.flex.items-start.gap-x-10.w-full > div.flex.flex-col.pt-\[7\.3rem\].lg\:pt-0.w-full.lg\:w-4\/5 > div > div:nth-child(1) > div.flex.flex-row.md\:flex-col.w-full.md\:w-1\/4.px-3.md\:px-6.pb-5.pt-2.lg\:py-7.md\:py-5.gap-4.h-full > div.hidden.md\:flex.justify-end.items-end.min-h-10 > button")  # Sesuaikan dengan XPath tombol
    book_button.click()
    time.sleep(5)
    print("Pemesanan hotel berhasil!")


def close_browser():
    driver.quit()

# Jalankan test
open_hotel_search_page()
book_hotel()
close_browser()
