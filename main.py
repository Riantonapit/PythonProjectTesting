from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maksimalkan jendela browser

driver = webdriver.Chrome(options=options)

def click_hotel_button():
    driver.get("https://stg.tixia.com/id")  # Ganti dengan URL OTA yang benar
    time.sleep(2)
    
    # Klik tombol hotel di homepage
    hotel_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[1]/div[2]/div/div/div[2]/a[2]")  # Sesuaikan dengan ID tombol hotel
    hotel_button.click()
    time.sleep(2)
    print("Tombol Hotel di homepage berhasil diklik.")
    
    # Temukan input pencarian dan masukkan lokasi
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[1]/div[2]/div/div/div[1]/button")
    button.click()
    button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/section/div[2]/div[1]/input")
    button.click()
    input_field.clear()
    input_field.send_keys("bali")
    time.sleep(5)
    
    # Pilih tanggal check-in dan check-out
    checkin_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[5]/button")  # Sesuaikan dengan ID input tanggal check-in
    checkout_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[6]/button")  # Sesuaikan dengan ID input tanggal check-out
    
    checkin_input.send_keys("15/03/2025")
    checkout_input.send_keys("17/03/2025")
    time.sleep(1)
    
    # Tekan tombol cari
    search_button = driver.find_element(By.ID, "search-button")  # Sesuaikan dengan ID tombol pencarian
    search_button.click()
    time.sleep(5)  # Tunggu hasil pencarian
    
    # Validasi hasil pencarian
    results = driver.find_elements(By.CLASS_NAME, "hotel-list-item")  # Sesuaikan dengan elemen yang benar
    assert len(results) > 0, "Tidak ada hasil yang ditemukan!"
    
    print("Pencarian hotel di Bali berhasil!")

def test_book_hotel():
    driver.get("https://dev.tixia.com/id")  # Ganti dengan URL OTA yang benar
    time.sleep(2)
    
    # Cari hotel di Bali
    test_search_hotel()
    
    # Pilih hotel pertama yang tersedia
    hotels = driver.find_elements(By.CLASS_NAME, "hotel-list-item")  # Sesuaikan dengan elemen hotel
    assert len(hotels) > 0, "Tidak ada hotel yang tersedia!"
    hotels[0].click()
    time.sleep(2)
    
    # Klik tombol pesan
    book_button = driver.find_element(By.ID, "book-hotel-button")  # Sesuaikan dengan ID tombol
    book_button.click()
    time.sleep(5)
    
    print("Pemesanan hotel berhasil!")

def click_button_by_id(button_id):
    button = driver.find_element(By.ID, button_id)
    button.click()
    time.sleep(2)
    print(f"Tombol dengan ID '{button_id}' berhasil diklik.")

def close_browser():
    driver.quit()

# Jalankan test
click_hotel_button()  # Klik tombol hotel terlebih dahulu
test_search_hotel()  # Lakukan pencarian setelah tombol hotel diklik
test_book_hotel()  # Lakukan pemesanan setelah hasil pencarian muncul
close_browser()
