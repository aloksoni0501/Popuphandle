from selenium import webdriver
import  unittest

import time
import HtmlTestRunner



class PopUpAlerts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("=========================Testing Start===========================")
        global driver
        cls.driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)

    def test_without_username(self):
        self.driver.get("https://mail.rediff.com")
        self.driver.find_element_by_xpath("//a[text()='Sign in']").click()
        self.driver.find_element_by_xpath("//input[@name='proceed']").click()

        time.sleep(2)

        self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.back()

        time.sleep(2)
    #   self.driver.back()
    #   time.sleep(2)
    #     self.driver.refresh()
    #     time.sleep(2)
    #     self.driver.forward()
    #
   # def test_login_valid(self):
    #
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_xpath("//*[@id='login1']").send_keys("aloksoni0501")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("alok@123")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@title='Sign in']").click()
    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()
        print("=====================Sucessfully logged in====================")

if __name__=="__main__":
         unittest.main()