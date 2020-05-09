import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Chrome/chromedriver.exe")
time.sleep(3)
driver.get("https://www.instagram.com/")

time.sleep(1)
usuario= ""
senha= ""

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(usuario)


driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(senha)

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()


