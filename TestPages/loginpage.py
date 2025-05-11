import time
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

curr_file_path = Path(__file__)
root_dir = curr_file_path.parent.parent.absolute()
print("root_dir", root_dir)
# class login():
#     def __init__(self):
#         service = Service(f"{root_dir}/Driver/chromedriver.exe")
#         option = Options()
#
#         # Create a new instance of the Chrome driver
#         driver = webdriver.Chrome(service=service)
#         driver.get("https://www.linkedin.com/login")  # get method to hit URL on browser
#         driver.maximize_window()
#         print(driver.title)
#         driver.quit()
#
# login()


if __name__ == "__main__":
    username_xpath = "//input[@id='username']"
    password_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@type='submit']"
    service = Service(f"{root_dir}/Driver/chromedriver.exe")
    option = Options()

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service, options=option)
    driver.get("https://www.linkedin.com/login")  # get method to hit URL on browser
    driver.maximize_window()
    print(driver.title)

    # try to login in linkedin app
    # enter username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, username_xpath))).send_keys("neha.surwase@gmail.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath))).send_keys("Neha@2894")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button_xpath))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-password-submit-button']"))).click()

    driver.quit()
