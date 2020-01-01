import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import contextlib
import selenium.webdriver.support.ui as ui

class Registration_physical (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_log_in(self):
        driver = self.driver
        driver.get("https://book24.ru")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element_by_link_text("Регистрация").click()
        driver.find_element_by_name("REGISTER[NAME]").click()
        driver.find_element_by_name("REGISTER[NAME]").send_keys("Сергей", Keys.ARROW_DOWN)
        driver.find_element_by_name("REGISTER[LAST_NAME]").click()
        driver.find_element_by_name("REGISTER[LAST_NAME]").send_keys("Иванов", Keys.ARROW_DOWN)
        driver.find_element_by_name("REGISTER[EMAIL]").click()
        driver.find_element_by_name("REGISTER[EMAIL]").send_keys("selsa123@mail.ru", Keys.ARROW_DOWN)
        driver.find_element_by_name("REGISTER[PERSONAL_PHONE]").click()
        driver.find_element_by_name("REGISTER[PERSONAL_PHONE]").send_keys("89637854990", Keys.ARROW_DOWN)
        driver.find_element_by_name("REGISTER[PERSONAL_BIRTHDAY]").click()
        driver.find_element_by_name("REGISTER[PERSONAL_BIRTHDAY]").send_keys("22.10.1999", Keys.ARROW_DOWN)

