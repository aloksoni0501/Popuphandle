
# Assertion in selenium Equal and NotEqual

from  selenium import webdriver

import unittest

class Assertion(unittest.TestCase):

    def test_assert(self):

        global driver

        driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        driver.maximize_window()
        driver.implicitly_wait(5)
    def test_title(self):

        driver.get("https://www.google.com")
        title_of_page = driver.title
        self.assertEqual("Google", title_of_page, "is not Equal")



        #driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
        #self.assertEqual("Google",titleofpage,"is not Equal")
       # self.assertEqual("Google12", titleofpage,"the title is not equal")

        #self.assertEqual("Google",titleofpage,"abc")
        driver.close()
        driver.quit()

if __name__=="__main__":
    unittest.main()
