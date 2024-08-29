from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.parametrs import kinopoisk_ui_url
import allure

class Kinopoisk:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(kinopoisk_ui_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step("Поиск фильма по названию")
    def search_film(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='kp_query']"))
        )
        self.driver.find_element(By.XPATH, "//input[@name='kp_query']").send_keys("Мстители")
        self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Найти') and contains(@class, 'styles_root')]").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space(text())='Мстители']"))
        )
        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Мстители']").click()
    
    @allure.step("Проверка фильма")
    def res_search_film(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space(text())='Мстители (2012)']").text
    
    @allure.step("Поиск актера")
    def search_actor(self):
        self.driver.find_element(By. XPATH, "//input[@name='kp_query']").send_keys("Роберт Дауни")
        self.driver.find_element(By. XPATH, "//button[contains(@aria-label, 'Найти') and contains (@class, 'styles_root')]").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Роберт Дауни мл.']").click()
    
    @allure.step("Проверка найденного актера")
    def res_search_actor(self):
        return self.driver.find_element(By. XPATH, "//h1[normalize-space(text())='Роберт Дауни мл.']").text
    
    @allure.step("Переход в онлайн-кинотеатр")
    def sport(self):
        self.driver.find_element(By. XPATH, "//div[contains(@class, 'styles_sticky__mDnbt')]//a[normalize-space(text())='Онлайн-кинотеатр']").click()

    @allure.step("Открытие списка фильмов по жанру Боевики")
    def militant(self):
        self.driver.find_element(By. XPATH, "//div[contains(@class, 'styles_sticky__mDnbt')]//a[normalize-space(text())='Фильмы']").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Жанры']").click()
        self.driver.find_element(By. XPATH, "//a[contains(concat(' ',@class,' '),'styles_root__c9qje') and normalize-space(.)='Боевики']").click()
    
    @allure.step("Проверка перехода к списку фильмов по жанру Боевики")
    def res_militant(self):
        return self.driver.find_element(By. XPATH, "//h1[contains(concat(' ',@class,' '),'styles_title__jB8AZ') and normalize-space(.)='Боевики – лучшие фильмы и сериалы']").text

    @allure.step("Поиск сериала и переход к списку актеров")
    def search_serial(self):
        self.driver.find_element(By. XPATH, "//input[@name='kp_query']").send_keys("Игра престолов")
        self.driver.find_element(By. XPATH, "//button[contains(@aria-label, 'Найти') and contains (@class, 'styles_root')]").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Игра престолов (сериал)']").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='В главных ролях']").click()

    @allure.step("Проверка актера из списка актеров сериала")
    def search_serial_actor(self):
        return self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Питер Динклэйдж']").text
        