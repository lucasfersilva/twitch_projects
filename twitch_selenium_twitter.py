import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Chrome/chromedriver.exe")
time.sleep(3)
driver.get("https://twitter.com/explore")

time.sleep(2)
usuario= "lucasfersilva"
senha= "lucas"

driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div[1]/div/div/div[1]/a/div").click()

driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(usuario)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(senha)
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()

