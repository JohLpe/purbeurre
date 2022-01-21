import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegistrationPage(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("http://127.0.0.1:8000/registration/")
        self.wait = self.driver.implicitly_wait(10)

    def test_registration_page(self):

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_username"]'
                                 ).send_keys("TestUsername")
        self.wait

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_first_name"]'
                                 ).send_keys("TestFirstname")
        self.wait

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_last_name"]'
                                 ).send_keys("TestLastname")
        self.wait

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_email"]'
                                 ).send_keys("TestUser@mail.com")
        self.wait

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_password1"]'
                                 ).send_keys("TestPassword")
        self.wait

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_password2"]'
                                 ).send_keys("TestPassword")
        self.wait

        self.driver.find_element(By.NAME, "Create user").click()
        self.wait

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
