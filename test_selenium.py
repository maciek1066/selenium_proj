from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_case1():
    path = "/home/mako/projects/selenium_proj/chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("http://www.seleniumhq.org/")
    elem = driver.find_element_by_link_text("Download")
    elem.click()
    search_box = driver.find_element_by_id("q")

    #  Sending text to html object
    search_box.send_keys('download')

    #  Using Keys
    # search_box.send_keys(Keys.ENTER)

    #  Using mouse click
    act = ActionChains(driver)
    act.click(driver.find_element_by_xpath(
        "//a[text()='edit this page']")).perform()


