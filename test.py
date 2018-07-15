from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import faker


data = faker.Faker()
path = "/home/mako/projects/selenium_proj/chromedriver"

driver = Chrome(executable_path=path)
driver.get("http://www.thetestingworld.com/testings")
myuser = driver.find_element_by_xpath("//input[@name='fld_username']")
myuser.send_keys(data.name())
email = driver.find_element_by_xpath("//input[@name='fld_email']")
email.send_keys(data.email())

#  password
password1 = driver.find_element_by_xpath("//input[@name='fld_password']")
password2 = driver.find_element_by_xpath("//input[@name='fld_cpassword']")
password_example = data.password()
password1.send_keys(password_example)
password2.send_keys(password_example)

# date = driver.find_element_by_xpath("//input[@name='dob']")
# date.send_keys(data.date())

phone = driver.find_element_by_xpath("//input[@name='phone']")
phone.send_keys(data.phone_number())
address = driver.find_element_by_xpath("//input[@name='address']")
address.send_keys(data.address())

#  Select on dropdown
gender = Select(driver.find_element_by_name("sex"))
gender.select_by_visible_text("Male")
country = Select(driver.find_element_by_name("country"))
country.select_by_visible_text("Poland")


# path = "/home/mako/projects/selenium_proj/chromedriver"
# driver = Chrome(executable_path=path)
# driver.get("https://www.webpagetest.org/")
#
# # Maximize browser
#
# driver.maximize_window()
#
# # Enter data to textbox
#
# driver.find_element_by_name("url")
# driver.find_element_by_xpath("//input[@name='url']").send_keys("www.amazon.com")
#
# # Work on dropdown
#
# obj = Select(driver.find_element_by_name("where"))
# obj.select_by_value("Mobile_Dulles_iPhone8")
#
# # Key strokes, act.click().perform() to click on target
#
# act = ActionChains(driver)
# act.send_keys(Keys.TAB).perform()
#
# act.send_keys(Keys.CONTROL).send_keys("a").perform()
