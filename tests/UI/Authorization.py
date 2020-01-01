import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import contextlib
import selenium.webdriver.support.ui as ui


class Auth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_log_in(self):
        driver = self.driver
        driver.get("https://demo.book24:book24@demo.book24.ru")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_xpath("(//input[@name=''])[2]").click()
        driver.find_element_by_xpath("(//input[@name=''])[2]").send_keys("selivanov.sa@eksmo.ru", Keys.ARROW_DOWN)
        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        driver.find_element_by_xpath("(//input[@name=''])[3]").send_keys("955098")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[@id='login']/div/form/div/div[5]/button").click()  # Клик по кнопке "Войти

        # driver.get ('https://demo.book24.ru/personal/my-library') # Переход на Отложенные

        # driver.find_element_by_link_text('Купить').click()
        driver.find_element_by_link_text('Оформить заказ').click()

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'ОФОРМИТЬ ЗАКАЗ'))
            )
        except TimeoutException as ex:
            print(ex.message)

        driver.find_element_by_partial_link_text('Оформить заказ').click()


# def tearDown(self):
#   self.driver.close()

if __name__ == "__main__":
    unittest.main()
