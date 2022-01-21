
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_registration_page(self):
         
        driver = self.driver
        driver.get("http://www.python.herokuapp.com/registration/")
 
        # assertion to confirm if title has python keyword in it
        self.assertIn("Python", driver.title)
 
        # locate element using name
        elem = driver.find_element_by_name("q")
 
        # send data
        elem.send_keys("pycon")
 
        # receive data
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
