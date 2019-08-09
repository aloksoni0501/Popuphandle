from selenium import webdriver
import  unittest

import time



class PopUpAlerts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_without_username(self):
        self.driver.get("https://mail.rediff.com")
        self.driver.find_element_by_xpath("//a[text()='Sign in']").click()
        self.driver.find_element_by_xpath("//input[@name='proceed']").click()

        time.sleep(4)
        self.driver.switch_to_alert().accept()
    @classmethod
    def test_tearDownClass(cls):
       #cls.driver.close()
        #cls.driver.quit()


if __name__=="__main__":
         unittest.main()