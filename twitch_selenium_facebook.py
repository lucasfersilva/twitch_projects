import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Chrome/chromedriver.exe")
time.sleep(3)
driver.get("https://www.facebook.com/")

time.sleep(2)
usuario= "lucasfersilva"
senha= "lucas"

driver.find_element_by_id("email").send_keys(usuario)

driver.find_element_by_id("pass").send_keys(senha)

driver.find_element_by_id('u_0_b').click()