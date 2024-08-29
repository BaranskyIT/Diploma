import requests
import allure

class Kinopoisk_Api:
    def __init__(self, url):
        self.url = url
    
    @allure.step("api. Получение информации о фильме по {id}")
    def search_film_id(self, id, headers):
        response = requests.get(self.url+'/movie/' + str(id), headers=headers)
        return response
    
    @allure.step("api. Получение информации о фильме по названию")
    def search_film_name(self, name, headers):
        my_params = {
            'page': '1',
            'limit': '10',
            'query': name
         }
        response = requests.get(self.url+'/movie/search?', params = my_params, headers=headers)
        return response
    
    @allure.step("api. Получение id фильма по рейтингу")
    def search_film_rating(self, rating, headers):
        my_params = {
            'page': '1',
            'limit': '10',
            'rating.kp': rating
         }
        response = requests.get(self.url+'/movie/search?', params = my_params, headers=headers)
        return response
    
    @allure.step("api. Получение фильма по жанру")
    def search_film_genres(self, genres_name, headers):
        my_params = {
            'page': '1',
            'limit': '10',
            'genres.name': genres_name
         }
        response = requests.get(self.url+'/movie/search?', params = my_params, headers=headers)
        return response
    

    @allure.step("api. Получение информации об актере по {id}")
    def search_actor_id(self, id, headers):
        response = requests.get(self.url+'/person/' + str(id), headers=headers)
        return response