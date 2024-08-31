from Pages.api_class import Kinopoisk_Api
from Pages.parametrs import api_key
from Pages.parametrs import kinopoisk_api_url
import pytest
import requests
import allure

api = Kinopoisk_Api(kinopoisk_api_url)
        
headers = {
"accept": "application/json",
"X-API-KEY": api_key
}    

@allure.epic("API")
@allure.severity(severity_level='normal')
@allure.title("Получение фильма по id")
@allure.description("Получение информации о фильме по id, проверка полученного id")
@allure.feature('Тест 1')
def test_search_film_id():
 with allure.step("Получить фильм по id"):
    res = api.search_film_id(263531, headers)
    id_film = res.json()['id']
 with allure.step("Проверка id полученного фильма"):
    assert id_film == 263531
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

@allure.epic("API")
@allure.severity(severity_level='normal')
@allure.title("Получение фильма по названию")
@allure.description("Получение информации о фильме по названию, проверка полученного названия")
@allure.feature('Тест 2')
def test_search_film_name():
 with allure.step("Получить фильм по названию"):
    res = api.search_film_name("Мстители", headers)
    film_name = res.json()['docs'][0]['name']
 with allure.step("Проверка названия полученного фильма"):
    assert film_name == 'Мстители'
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

@allure.epic("API")
@allure.severity(severity_level='normal')
@allure.title("Получение id фильма по рейтингу")
@allure.description("Получение id фильма по рейтингу и его проверка")
@allure.feature('Тест 3')
def test_search_film_rating():
 with allure.step("Получение id фильма по рейтингу"):
    resp = api.search_film_rating(8, headers)
    response = resp.json()['docs'][0]['id']
 with allure.step("Проверка id"):
    assert response == 535341
 with allure.step("Проверка статус кода"):
    assert resp.status_code == 200

@allure.epic("API")
@allure.severity(severity_level='normal')
@allure.title("Получение информации о фильме по жанру")
@allure.description("Получение информации о фильме по жанру и его проверка")
@allure.feature('Тест 4')
def test_search_film_genres():
 with allure.step("Получение информации о фильме по жанру"):
    res = api.search_film_genres("комедия", headers)
    genres_id = res.json()['docs'][0]['id']
    genres_name = res.json()['docs'][0]['name']
 with allure.step("Проверка id и названия фильма"):
    assert genres_id == 535341
    assert genres_name == '1+1'
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

@allure.epic("API")
@allure.severity(severity_level='normal')
@allure.title("Получение информации об актере по id")
@allure.description("Получение информации об актере по id и его проверка")
@allure.feature('Тест 5')
def test_search_actor_id():
 with allure.step("Получение информации об актере по id"):
    res = api.search_actor_id(10096, headers)
    actor_id = res.json()['id']
    actor_name = res.json()['name']
 with allure.step("Проверка id и имени актера"):
    assert actor_id == 10096
    assert actor_name == 'Роберт Дауни мл.'
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

