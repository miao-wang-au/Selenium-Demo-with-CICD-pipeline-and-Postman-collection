import time
from datetime import date

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")

driver.find_element(By.NAME, "username").send_keys("f4fadmin@f4f.com")
driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB")

# XPATH -> //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -> tagname[attribute='value'] -> //input[type='submit']

driver.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@data-testid='selectSupplier13']"))
)
driver.find_element(By.XPATH, "//button[@data-testid='selectSupplier13']").click()

WebDriverWait(driver, 5)

driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click() # The only way that has worked so far

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@title='Open']"))
)

driver.find_element(By.XPATH, "//button[@title='Open']").click()

# Click dropdown 'mater Private Hospital'
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]"))
)
driver.find_element(By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]").click()



WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.LINK_TEXT, "Requisitions"))
)

driver.find_element(By.LINK_TEXT, "Requisitions").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(6) button:nth-child(2)"))
)

driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(6) button:nth-child(2)").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[44]"))
)

driver.find_element(By.XPATH, "(//button[@type='button'])[44]").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]"))
)

releasemessage = driver.find_element(By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]").text

print(releasemessage)