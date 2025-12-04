import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from UserLogin import Login
from Add3Items import AddThreeItems


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_stock_release_workflow(driver):
    # ---------------- Login as Hospital Theater ----------------
    driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")
    Login("Hospital Theater", driver)

    # Navigate to Stock Levels > Consignment
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Stock Levels')]"))
    ).click()
    driver.find_element(By.LINK_TEXT, "Consignment").click()

    # Wait for table to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//tbody/tr[6]/td[4]"))
    )

    StockScan = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]").text
    StockManual = driver.find_element(By.XPATH, "//tbody/tr[5]/td[4]").text
    StockSearch = driver.find_element(By.XPATH, "//tbody/tr[6]/td[4]").text

    print(f"Stock before release: 430005S={StockScan}, 430004S={StockManual}, 430003S={StockSearch}")

    # ---------------- Add three items ----------------
    driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]").click()
    AddThreeItems(driver)

    # Wait for requisition alert
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@role='alert'])[1]"))
    )
    RequisitionCreated = driver.find_element(By.XPATH, "(//div[@role='alert'])[1]").text
    print(RequisitionCreated)

    # Logout Hospital Theater
    driver.find_element(By.XPATH, "(//button[@title='Account settings'])[1]").click()
    driver.find_element(By.XPATH, "(//li[normalize-space()='Logout'])[1]").click()

    # ---------------- Login as Customer Service ----------------
    Login("Customer Service", driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Requisitions"))
    ).click()

    # Open the requisition
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[10]"))
    ).click()

    # Click Release button
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '(//button[contains(@class, "MuiButton-containedPrimary") '
                                              'and normalize-space()="Release"])[3]'))
    ).click()

    # Wait for release success message
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]"))
    )
    releasemessage = driver.find_element(By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]").text
    print(releasemessage)

    # ---------------- Verify stock after release ----------------
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-9'])[2]"))
    ).click()
    driver.find_element(By.LINK_TEXT, "Consignment").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//tbody/tr[6]/td[4]"))
    )

    StockScanReleased = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]").text
    StockManualReleased = driver.find_element(By.XPATH, "//tbody/tr[5]/td[4]").text
    StockSearchReleased = driver.find_element(By.XPATH, "//tbody/tr[6]/td[4]").text

    print(f"Stock after release: 430005S={StockScanReleased}, 430004S={StockManualReleased}, 430003S={StockSearchReleased}")

    # Assertions
    assert int(StockScan) - int(StockScanReleased) == 1
    assert int(StockManual) - int(StockManualReleased) == 0
    assert int(StockSearch) - int(StockSearchReleased) == 1

    print("Regression Scenario 1 before CD message Successfully Executed")
