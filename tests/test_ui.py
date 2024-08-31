from Pages.ui_class import Kinopoisk
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import allure

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

@allure.epic("TEST UI")
@allure.severity(severity_level='normal')
@allure.title("Поиск фильма")
@allure.description("Поиск фильма и его проверка")
@allure.feature('Тест 1')
def test_search_film():
 with allure.step("Открытие Кинопоиска и поиск фильма"):
    ui_class = Kinopoisk(driver)
    ui_class.search_film()
 with allure.step("Проверка найденого фильма"):
    response = ui_class.res_search_film()
    assert response == "Мстители (2012)"

@allure.epic("TEST UI")
@allure.severity(severity_level='normal')
@allure.title("Поиск актера")
@allure.description("Поиск актера и его проверка")
@allure.feature('Тест 2')
def test_search_actor():
 with allure.step("Открытие Кинопоиска и поиск актера"):
    ui_class = Kinopoisk(driver)
    ui_class.search_actor()
 with allure.step("Проверка найденного актера"):
    response = ui_class.res_search_actor()
    assert response == "Роберт Дауни мл."

@allure.epic("TEST UI")
@allure.severity(severity_level='normal')
@allure.title("Переход в онлайн-кинотеатр")
@allure.description("Переход в онлайн-кинотеатр")
@allure.feature('Тест 3')
def test_online():
 with allure.step("Открытие интернет-сервиса и переход в онлайн-кинотеатр"):
    ui_class = Kinopoisk(driver)
    ui_class.sport()
 with allure.step("Проверка открытого url"):
    url = driver.current_url
    assert url == "https://hd.kinopoisk.ru/"

@allure.epic("TEST UI")
@allure.severity(severity_level='normal')
@allure.title("Переход к Боевикам")
@allure.description("Переход к списку фильмов по жанру Боевики")
@allure.feature('Тест 4')
def test_ticket():
 with allure.step("Открытие Кинопоиска и переход в раздел Фильмы"):
    ui_class = Kinopoisk(driver)
    ui_class.militant()
 with allure.step("Проверка перехода к списку фильмов жанра Боевики"):
    response = ui_class.res_militant()
    assert response == "Боевики – лучшие фильмы и сериалы"

@allure.epic("TEST UI")
@allure.severity(severity_level='normal')
@allure.title("Поиск сериала и переход к списку актеров")
@allure.description("Поиск сериала, октрытие списка актеров и проверка одного актера")
@allure.feature('Тест 5')
def test_serial_search():
 with allure.step("Открытие кинопоиска, переход к сериалу и открытие списка актеров сериала"):
    ui_class = Kinopoisk(driver)
    ui_class.search_serial()
 with allure.step("Проверка актера"):
    res = ui_class.search_serial_actor()
    assert res == "Питер Динклэйдж"
    driver.quit()

