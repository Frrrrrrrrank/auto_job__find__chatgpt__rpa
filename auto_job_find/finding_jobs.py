import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局 WebDriver 实例
driver = None


def get_driver():
    global driver
    return driver


def open_browser_with_options(url, browser):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    else:
        raise ValueError("Browser type not supported")

    driver.get(url)

    # 等待直到页面包含特定的 XPath 元素
    xpath_locator = "//*[@id='header']/div[1]/div[3]/div/a"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator))
    )

def log_in():
    global driver

    # 点击按钮
    login_button = driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div[3]/div/a")
    login_button.click()

    # 等待微信登录按钮出现
    xpath_locator_wechat_login = "//*[@id='wrap']/div/div[2]/div[2]/div[2]/div[1]/div[4]/a"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_wechat_login))
    )

    wechat_button = driver.find_element(By.XPATH, "//*[@id='wrap']/div/div[2]/div[2]/div[2]/div[1]/div[4]/a")
    wechat_button.click()

    xpath_locator_wechat_logo = "//*[@id='wrap']/div/div[2]/div[2]/div[1]/div[2]/div[1]/img"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_wechat_logo))
    )

    xpath_locator_login_success = "//*[@id='header']/div[1]/div[3]/ul/li[2]/a"
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_login_success))
    )

def get_job_description():

    global driver

    # 使用给定的 XPath 定位职位描述元素
    xpath_locator_job_description = "//*[@id='wrap']/div[2]/div[2]/div/div/div[2]/div/div[2]/p"

    # 确保元素已加载并且可以获取文本
    job_description_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_job_description))
    )

    # 获取职位描述文本
    job_description = job_description_element.text
    print(job_description)  # 打印出职位描述，或者你可以在这里做其他处理

    # 返回职位描述文本，如果函数需要
    return job_description

def select_dropdown_option(driver, label):
    # 确保触发下拉列表的元素可见并且可点击
    trigger_selector = "//*[@id='wrap']/div[2]/div[1]/div/div[1]/div"
    trigger_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, trigger_selector))
    )
    trigger_element.click()  # 打开下拉菜单

    # 等待下拉列表元素变为可见
    dropdown_selector = "ul.dropdown-expect-list"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_selector))
    )

    # 现在点击下拉列表中的具体选项
    option_selector = f"//li[contains(text(), '{label}')]"
    option_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, option_selector))
    )
    option_element.click()  # 选择下拉菜单中的选项


def get_job_description_by_index(index):
    try:
        job_selector = f"//*[@id='wrap']/div[2]/div[2]/div/div/div[1]/ul/li[{index}]"
        job_element = driver.find_element(By.XPATH, job_selector)
        job_element.click()

        description_selector = "//*[@id='wrap']/div[2]/div[2]/div/div/div[2]/div/div[2]/p"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, description_selector))
        )
        job_description_element = driver.find_element(By.XPATH, description_selector)
        return job_description_element.text

    except NoSuchElementException:
        print(f"No job found at index {index}.")
        return None

# Variables
url = "https://www.zhipin.com/web/geek/job-recommend?ka=header-job-recommend"
browser_type = "chrome"



