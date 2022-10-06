import time
from selenium import webdriver


class Locator:
    button_main = ('xpath', '//li[@id="menu-item-1194"]')
    button_description = ('xpath', '//li[@id="menu-item-1243"]')
    button_federal_programm = ('xpath', '//li[@id="menu-item-22243"]')
    button_applicants = ('xpath', '//li[@id="menu-item-1557"]')
    button_students = ('xpath', '//li[@id="menu-item-1246"]')
    button_institutes = ('xpath', '//li[@id="menu-item-3201"]')
    button_it_cube = ('xpath', '//li[@id="menu-item-24859"]')
    button_contacts = ('xpath', '//li[@id="menu-item-22570"]')
    button_request = ('xpath', '//li[@id="menu-item-16218"]')


class AnyPage(Locator):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ngieu.ru/')

    def click_button_main(self):
        """Нажатие на кнопку 'Главная'"""
        self.driver.find_element(Locator.button_main)
        time.sleep(2)
        return

    def click_button_description(self):
        self.driver.find_element('xpath', '//li[@id="menu-item-1243"]').click()
        time.sleep(2)
        return 'https://ngieu.ru/sveden/'

    def click_button_federal_programm(self):
        self.driver.find_element(Locator.button_federal_programm)
        time.sleep(2)
        return

    def click_button_applicants(self):
        self.driver.find_element(Locator.button_applicants)
        time.sleep(2)
        return

    def click_button_students(self):
        self.driver.find_element(Locator.button_students)
        time.sleep(2)
        return

    def click_button_institutes(self):
        self.driver.find_element(Locator.button_institutes)
        time.sleep(2)
        return

    def click_button_it_cube(self):
        self.driver.find_element(Locator.button_it_cube)
        time.sleep(2)
        return

    def click_button_contacts(self):
        self.driver.find_element(Locator.button_contacts)
        time.sleep(2)
        return

    def click_button_request(self):
        self.driver.find_element(Locator.button_request)
        time.sleep(2)
        return

