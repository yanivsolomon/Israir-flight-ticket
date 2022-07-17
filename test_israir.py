from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import Select

# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield
    driver.close()
    driver.quit()
    print("test completed")

# starting the test
def test_reservation(test_setup):
    driver.get("https://www.israir.co.il/")
    driver.implicitly_wait(5)
# closing the popup
    popupcatch = driver.find_element_by_xpath("//button[@aria-label='סגירה']")
    popupcatch.click()
# closing the cookie footer
    cookiecatch = driver.find_element_by_class_name("CookieMessage__closeBtn")
    cookiecatch.click()
    time.sleep(2)

    flightonly = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/li[1]/section[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/label[2]")
    flightonly.click()
    time.sleep(2)

    onedirection = driver.find_element_by_xpath("//body/div[2]/div[2]/div[1]/div[1]/li[1]/section[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[2]/label[2]")
    onedirection.click()
    time.sleep(2)

    search_that_flight = driver.find_element_by_xpath("//button[contains(text(),'חפש לי חופשה')]")
    search_that_flight.click()
    time.sleep(5)
# next screen - choose a flight (book now)
    book_now = driver.find_element_by_xpath("//body/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[3]/div[1]/div[2]/button[2]")
    book_now.click()
# New screen - Personal details
    time.sleep(8)
    first_name = driver.find_element_by_xpath("//input[@id='fname0']")
    first_name.send_keys("Tester")

    last_name = driver.find_element_by_xpath("//input[@id='lname0']")
    last_name.send_keys("Testoni")

    # identify dropdown with Select class - year
    sel = Select(driver.find_element_by_xpath("//select[@id='year0']"))
    # select by select_by_visible_text() method
    sel.select_by_visible_text("1991")

# identify dropdown with Select class - month
    sel = Select(driver.find_element_by_xpath("//select[@id='month0']"))
    # select by select_by_visible_text() method
    sel.select_by_visible_text("08")

# identify dropdown with Select class - day
    sel = Select(driver.find_element_by_xpath("//select[@id='day0']"))
    sel.select_by_visible_text("14")

    passport = driver.find_element_by_id("passportNo0")
    passport.send_keys("445005888")

    # identify dropdown with Select class - passport year
    sel = Select(driver.find_element_by_xpath("//select[@id='yearExpiration0']"))
    sel.select_by_visible_text("2027")

    # identify dropdown with Select class - passport month
    sel = Select(driver.find_element_by_xpath("//select[@id='monthExpiration0']"))
    sel.select_by_visible_text("08")

    # identify dropdown with Select class - passport day
    sel = Select(driver.find_element_by_xpath("//select[@id='dayExpiration0']"))
    sel.select_by_visible_text("14")

    phone = driver.find_element_by_id("phone0")
    phone.send_keys("0545408862")

    email = driver.find_element_by_id("email0")
    email.send_keys("teston@walla.com")

# checkboxes
    first_checkbox = driver.find_element_by_xpath("//body/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]")
    first_checkbox.click()
    second_checkbox = driver.find_element_by_xpath("//body/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/label[1]")
    second_checkbox.click()
    third_checkbox = driver.find_element_by_xpath("//body/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/label[1]")
    third_checkbox.click()
    forth_checkbox = driver.find_element_by_xpath("//body/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/label[1]")
    forth_checkbox.click()
    fifth_checkbox = driver.find_element_by_xpath("//body/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/label[1]")
    fifth_checkbox.click()

    #pick a seat
    pick_seat = driver.find_element_by_xpath("//input[@id='paxLegSeat00']")
    pick_seat.click()
    time.sleep(3)
    # iframe element - pick a seat
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='seatMapContent']"))
    driver.find_element_by_xpath("//tbody/tr[1]/td[2]/ul[1]/li[25]/ul[1]/li[3]/span[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[contains(text(),'סיימתי')]").click()
    time.sleep(3)
    driver.switch_to.default_content()
    time.sleep(2)

#    final checkboxes
    final_checkbox1 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/footer[1]/ul[1]/li[1]/label[1]")
    final_checkbox1.click()
    final_checkbox2 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/footer[1]/ul[1]/li[2]/label[1]")
    final_checkbox2.click()
    final_checkbox3 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/footer[1]/ul[1]/li[3]/label[1]")
    final_checkbox3.click()
    final_checkbox4 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/footer[1]/ul[1]/li[4]/label[1]")
    final_checkbox4.click()
    final_checkbox5 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/footer[1]/ul[1]/li[5]/label[1]")
    final_checkbox5.click()
# order button
    order_btn = driver.find_element_by_xpath("//button[contains(text(),'הזמן')]")
    order_btn.click()
    time.sleep(5)

# next screen - payment (outside leading code iframe)
    driver.switch_to.frame(driver.find_element_by_id("paymentFrame"))
    credit_card = driver.find_element_by_xpath("//input[@id='card-number']")
    credit_card.send_keys("3566000020000410")
# dropdown year
    sel2 = Select(driver.find_element_by_xpath("//select[@id='expYear']"))
    sel2.select_by_visible_text("2023")
# dropdown month
    sel3 = Select(driver.find_element_by_xpath("//select[@id='expMonth']"))
    sel3.select_by_visible_text("02")
# cvv
    cvv_number = driver.find_element_by_xpath("//input[@id='cvv']")
    cvv_number.send_keys("123")
# id
    id_number = driver.find_element_by_xpath("//input[@id='personal-id']")
    id_number.send_keys("304450830")
# pay button
    pay_button = driver.find_element_by_xpath("//button[@id='cg-submit-btn']")
    pay_button.click()
    time.sleep(8)