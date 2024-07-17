import time
from UserLogin import Login
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddThreeItems:
    def __init__(self, a):
        self.driver = a

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Create Requisition Order')]"))
        )

        # Click button 'Create Requisition Order'
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Create Requisition Order')]").click()

        # Click Select Cost Center dropdown
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@title='Open'])[2]"))
        )
        self.driver.find_element(By.XPATH, "(//button[@title='Open'])[2]").click()

        self.driver.find_element(By.XPATH, "//*[contains(text(), 'code3')]").click()

        self.driver.find_element(By.ID, "consignment-invoice").click()

        self.driver.find_element(By.CSS_SELECTOR, "#text-field-id-0-0").send_keys("010454654041896817250331241UBI00012£10lot500")

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value((By.XPATH, "(//input[@id='text-field-id-0-1'])[1]"), 'lot500')
        )

        self.driver.find_element(By.XPATH, "(//input[@id='text-field-id-0-2'])[1]").send_keys(
            "{}".format("{}".format(datetime.now().strftime("%d%m%Y%H%M%S"))))

        self.driver.find_element(By.XPATH, "(//button[@id='submitButton'])[1]").click()

        # search tab
        self.driver.find_element(By.XPATH, "//button[@data-testid='tab-1']").click()

        self.driver.find_element(By.ID, "dropdown-field-id-0-0").send_keys("430003S")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '430003S')]"))
        )

        self.driver.find_element(By.XPATH, "//*[contains(text(), '430003S')]").click()

        self.driver.find_element(By.ID, "select-id-0-2").click()

        self.driver.find_element(By.XPATH, "//option[@data-testid='options-0-2-2']").click()

        self.driver.find_element(By.XPATH, "(//button[@id='submitButton'])[1]").click()

        # Manual tab

        self.driver.find_element(By.XPATH, "(//button[@role='tab'])[3]").click()

        self.driver.find_element(By.XPATH, "(//input[@id='dropdown-field-id-0-0'])[1]").send_keys("430004S")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '430004S')]"))
        )

        self.driver.find_element(By.XPATH, "//*[contains(text(), '430004S')]").click()

        self.driver.find_element(By.XPATH, "(//input[@id='text-field-id-0-1'])[1]").send_keys(
            "{}".format("{}".format(datetime.now().strftime("%d%m%Y%H%M%S"))))

        self.driver.find_element(By.XPATH, "(//input[@id='toDate'])[1]").send_keys("2025-05-11")

        self.driver.find_element(By.XPATH, "(//button[@id='submitButton'])[1]").click()

        self.driver.find_element(By.CSS_SELECTOR, "#submitButton").click()

        self.driver.find_element(By.XPATH, "(//button[@type='button'])[15]").click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='text-field-id'])[2]"))
        )

        self.driver.find_element(By.XPATH, "(//input[@id='text-field-id'])[2]").send_keys("1234")

        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "svg[data-testid='valid-pin-check']"))
        )

        self.driver.find_element(By.XPATH, "(//button[@type='button'])[17]").click()



# driver = webdriver.Chrome()
# driver.set_window_position(2000, 0)
# driver.maximize_window()
# driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")
#
# Login("Hospital Theater", driver)
#
# AddThreeItems(driver)
