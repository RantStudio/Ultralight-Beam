import unittest
from selenium import webdriver


class TestOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_url(self):
        self.driver.get("https://soundcloud.com/")
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/input').send_keys("carti")
        self.driver.find_element_by_xpath("""//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/button""").click()
        print(self.driver.current_url)
        self.assertIn(
            "https://soundcloud.com/search?q=carti", self.driver.current_url
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
