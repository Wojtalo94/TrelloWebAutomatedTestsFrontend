import requests
import logging
from tools.user_data import UserData


class Request():
    def __init__(self):
        self._logger = logging.getLogger("Request")
        _user_data = UserData("tools/user_data.csv")
        _api_key = _user_data.get_user_data("TRELLO_API_KEY")
        _api_token = _user_data.get_user_data("TRELLO_API_TOKEN")
        _query_string = f"?key={_api_key}&token={_api_token}"
        _id = self.get_board_id(_query_string)
        self._urls = {"trello_user": f"https://api.trello.com/1/members/me/{_query_string}",
                      "boards_members": f"https://api.trello.com/1/boards/{_id}/memberships{_query_string}"}
    
    def url(self, name: str):
        if not name in self._urls:
            raise AttributeError(f"Missing {name} in urls list")
        return self._urls[name]

    def _prepare_return(self, response):
        try:
            data = response.json()
        except:
            data = {}
        return data, response.status_code

    def get(self, url: str):
        with requests.Session() as s:
            return self._prepare_return(s.get(url, proxies=None))

    def patch(self, url: str, json: dict):
        with requests.Session() as s:
            return self._prepare_return(s.patch(url, json=json, proxies=None))

    def put(self, url: str, json=None):
        with requests.Session() as s:
            return self._prepare_return(s.put(url, json=json, proxies=None))

    def post(self, url: str, json: dict):
        with requests.Session() as s:
            return self._prepare_return(s.post(url, json=json, proxies=None))

    def delete(self, url: str):
        with requests.Session() as s:
            return self._prepare_return(s.delete(url, proxies=None))
    
    def get_all_boards_data(self, _query_string):
        response = self.get(f"https://api.trello.com/1/members/me/boards/{_query_string}")
        return response
    
    def get_all_boards_members(self):
        response = self.get(self.url("boards_members"))
        return response
    
    def get_board_id(self, _query_string):
        self._logger.info("Get board id for next requests")
        response, _ = self.get_all_boards_data(_query_string)
        first_board_id = response[0]['id']
        return first_board_id