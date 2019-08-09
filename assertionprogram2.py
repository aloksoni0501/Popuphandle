from  selenium import webdriver

import unittest
import HtmlTestRunner
class Assertion2(unittest.TestCase):

    def test_assert2(self):

        global driver

        driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")

        driver.maximize_window()
        driver.implicitly_wait(5)
       # self.assertIsNone(url)
       # self.assertIsNotNone(url)
    def test_title2(self):

        driver.get("https://www.google.com")
        #titleofpage2 = driver.title
        # self.assertEqual("https://www.google.com", url,"it is not Equal")

        driver.find_element_by_xpath("//*[@name='q']").send_keys("facebook.com")


        driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()

        # self.assertEqual("Google",titleofpage)
       # self.assertEqual("Google12", titleofpage,"the title is not equal")

        #self.assertNotEqual("Google12",titleofpage)
        #self.assertIsNone(url)
       # self.assertEqual("https://www.google.com", url,"it is not Equal")
        driver.close()
        driver.quit()


        self.driver.assertIsNotNone()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())