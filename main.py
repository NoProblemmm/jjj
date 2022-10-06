import time
from selenium import webdriver


class MainPage:

    def send_keys_search_input(self, driver, text):
        driver.find_element('xpath', '//input[@class="gLFyf gsfi"]').send_keys(text)

    def click_button_submit(self, driver):
        driver.find_element('xpath', '//input[@class="gNO89b"]').click()

    def clear_search_input(self, driver123):
        driver.find_element('xpath', '//input[@class="gLFyf gsfi"]').clear()33

    def click_button_random(self, driversss):
        driver.find_element('xpath', '//div[@class="FPdoLc lJ9FBc"]//input[@class="RNmpXc"]').click()


def test_selenium():
    driver = webdriver.Chrome()
    driver.get('https://www.google.ru/')
    main_page = MainPage()

    main_page.click_button_random(driver)
    time.sleep(5)
    driver.quit()
    print('123123')
    print('123123123')
    print('1232123123123')

if __name__ == '__main__':
    test_selenium()

